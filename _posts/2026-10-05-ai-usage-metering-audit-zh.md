---
layout: post
title: "我们审计了 110 个 AI 用量工具：数字都在哪里出错"
subtitle: "五个 bug 家族、一次独立复现、23 个上游合并，以及发布后第一个外部真实案例。"
date: 2026-10-05 10:00:00 +0800
lang: zh-CN
reading_time: 5
tags: ["Agent", "AgentMeasure", "计量", "开源"]
description: "AI 产品的计费正在从包月转向按量与按结果，每个数字都出自一只表（meter），表多半握在厂商手里。过去一个月，我们审计了开源侧数 token、算成本、管预算的 110 个 AI 用量工具。核心判断先…"
permalink: /notes/ai-usage-metering-audit-zh/
---

AI 产品的计费正在从包月转向按量与按结果，每个数字都出自一只表（meter），表多半握在厂商手里。过去一个月，我们审计了开源侧数 token、算成本、管预算的 110 个 AI 用量工具。核心判断先给：45+ 个已验证 bug，收敛成五个反复出现的家族；23 个修复已合并进上游，其中包括 34k star 的 langfuse；一位外部开发者复现了全部 236 项检查，还量化出一条路径把用量少报约 99%（见[审计正本](https://github.com/roy-tong/AgentMeasure/blob/main/campaigns/audit-report-2026-09.md)）。这些 bug 都不精巧，但每一个都会顺着聚合链传进账单最底下那行数字。

## 表在厂商手里

[《每个 Agent 用量数字，都是自报的》](/notes/every-agent-usage-number-is-self-reported-zh/)审的是发布数字的人；这一篇往里一层，去审制造数字的表。开源代码可读、bug 可验证，暴露的问题模式商业产品没有理由免疫。

为什么是现在，三个事实够了。2026-06-15，Salesforce 签最终协议，以约 $3.6B 收购 Intercom 旗下的客服 Agent Fin，其 $400M 年化收入中约 $100M 来自按解决计费（[Salesforce 投资者公告](https://investor.salesforce.com/news/news-details/2026/Salesforce-Signs-Definitive-Agreement-to-Acquire-Fin/default.aspx)、[RTE](https://www.rte.ie/news/business/2026/0615/1578570-salesforce-agrees-to-buy-irish-tech-firm-fin-for-36bn/)；签约时交易尚待监管批准）；Zendesk 重构为按「Verified Resolution」计费，判定用的模型和标准都是 Zendesk 自家的（[Zendesk 帮助中心](https://support.zendesk.com/hc/en-us/articles/9570369117338-About-automated-resolution-tiers)、[TechRadar](https://www.techradar.com/pro/zendesk-links-ai-pricing-to-verified-resolution-outcomes)）；HubSpot 把 Breeze Customer Agent 改为每条已解决对话 $0.50，定义是「无人工转接的对话」（[HubSpot 官方新闻](https://www.hubspot.com/company-news/hubspots-customer-agent-and-prospecting-agent-now-you-pay-when-the-task-is-complete)）。

名义单位相同，价格并不等价：Clelp 的算例里，同样每月 10 万次 resolution，Fin 与 Zendesk 一年差出约 $612K（[Clelp](https://clelp.ai/blog/outcome-based-ai-pricing-nobody-audits-the-outcome)）。**vendor runs the meter**——运行表的、定单位的、寄账单的，是同一家。

## 审计方法

审计面有四条：价表、缓存桶、流式聚合、去重。铁律一条，real-data-first——先用真实数据、后用合成数据——每条声称都附带可复现的检查命令（审计正本）。三条纪律，各自对应一族 bug：分类先于归一化，先确定事件是什么再算它值多少钱；声称的计费路径逐桶核对，厂商说怎么算就按厂商说的对；窗口与夹具锚定，时间窗口和测试夹具显式固定。

## 五个 bug 家族，五个具体例子

先给全景：

| # | 家族 | 一句话描述 | 直接后果 |
|---|---|---|---|
| 1 | 价表陈旧 | 价表缺当前模型代际 | 下游所有汇总继承错误 |
| 2 | 缓存乘数错厂商 | 一家的乘数套给所有厂商 | 每行看着都对，总数错 |
| 3 | 重发塌缩 | 字节级重试被重复计入 | 双计，或反向漏计 |
| 4 | absent 当 zero | 缺失字段读成 0 | 「未知」变成「免费」 |
| 5 | 窗口语义 | 挂钟锚定加绝对日期夹具 | 测试全绿，某天集体失效 |

### 家族一：价表陈旧——七个体检，五个不合格

最常见也最无聊：价表里没有当前代际的模型。一批七个工具里，五个的费率行已过期或缺失（审计正本）。工具不知道自己不知道，下游汇总原样继承这份错误。

### 家族二：缓存乘数错厂商——Anthropic 的折扣套在 OpenAI 头上

各厂商对缓存的读写按不同乘数计费，常见捷径是把一家的比率硬编码套给所有人。抓到过一个工具，把 Anthropic 的 cache-read 折扣乘数应用在 OpenAI 模型上，缓存读被算成实际计费量的约五分之一（审计正本）。最麻烦的是每一行单看都合理，逐行对账没有一行会报警。

### 家族三：重发塌缩——46% 的重发是字节级重复

流式请求重试时，两次尝试若字节级相同，一部分聚合器会把两次都计上。一份 604 个重发事件的公开语料里，46% 的重发是字节级重复；如果聚合器不识别 attempt identity，这部分事件会被按两次工作量计入（审计正本含复现命令）。

### 家族四：absent 被当成 zero

usage 字段缺失时，代码里一个 `or 0` 就把「未知」翻译成了「免费」。读起来像防御性编程，行为上像一笔没人授权的折扣。这问题没法在语法层面修：absent 必须保持 absent，聚合层要允许输出 UNPROVABLE，而不是被迫交出一个 0。

商业计费里有一条值得并排看的规则：Intercom 的 Fin 把「客户沉默离场」明文计为 assumed resolution 并照常计费（[Intercom 帮助文档 8205718](https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes)）；社区里有买家自报 confirmed resolution 6–7%、assumed 近 60%——缺失的客户回应，被表读成了收入（[Intercom 社区帖 8268](https://community.intercom.com/analyze-fin-93/how-do-you-improve-your-confirmed-resolution-rate-8268)）。它们共享的不是同一种 bug，而是同一个计量风险，系统必须把『未知状态如何映射成计费状态』显式写进规则。

### 家族五：窗口语义——我们自己的 CI 踩过的坑

配额窗口锚定在挂钟时间上，测试夹具又钉死了绝对日期，于是测试可以连续 30 天全绿，然后在同一天全线失效。这个例子由我们自己贡献：我们的 CI 就这么坑过我们一次（审计正本）。

## 独立复现

一位外部开发者独立复现了整套一致性测试——236 项检查全部复现——又量化了商业可观测厂商 AgentOps 的缓存计费：四条代码路径失败，受影响路径用量分别少报 98.9% 和 95.1%，问题钉到具体 commit（[证据卡](https://github.com/roy-tong/AgentMeasure/tree/main/conformance/evidence/agentops-anthropic-cache-drop-independent)，commit [010ba15](https://github.com/roy-tong/AgentMeasure/commit/010ba15) 入库）。

## 23 个上游合并：维护者用代码投票

审计留下的指纹，是 23 个已合并进上游的修复：价表更新、按厂商修正的缓存乘数、带回归夹具的重发塌缩防护、显式化的 absent-vs-zero 语义，落点包括 langfuse（34k star）和 codeburn（11k star）（[英文完整稿](https://dev.to/roytong/we-audited-110-ai-usage-tools-here-is-where-the-numbers-go-wrong-5d8h)）。每一条都始于维护者已在讨论的 thread，我们只是带着可复现的检查加了进去。merge 不是点赞，是维护者拿自己的代码投的票。

## 发布后的第一个真实案例

报告发布之后，第一个从外部浮现的真实案例落进了证据库。rulestack 的用量记录公开可查，账本上有一笔工作计了 436k tokens，独立重算的结果是 54,154——约 8 倍的差。原因不在价表，在缓存的计费语义：同一份重放的缓存前缀（cache prefix），每次 spawn 都被当作新输入重新计费。这个案例走的路，是每笔计费争议都该走的路——主张、重算、引用来源。判定与逐条数据在[证据卡](https://github.com/roy-tong/AgentMeasure/tree/main/conformance/evidence)，完整记录见[审计报告](https://github.com/roy-tong/AgentMeasure/blob/main/campaigns/audit-report-2026-09.md)（[英文完整稿](https://dev.to/roytong/we-audited-110-ai-usage-tools-here-is-where-the-numbers-go-wrong-5d8h)）。

## 厂商该公布的两样东西

我们还查了 20 家商业厂商，只查表计错了之后怎么办：公开的争议路径或更正政策，任何一种。在我们核查的这 20 家的公开文档里，截至 2026-09 没有找到任何一种（[英文完整稿](https://dev.to/roytong/we-audited-110-ai-usage-tools-here-is-where-the-numbers-go-wrong-5d8h)）。当厂商运行着表、给自己的作业打分、又不公布更正流程时，「相信我们」就是全部的内控体系。两条最低标准：一条具名的争议路径，一份机器可校验的计费披露。

## 自查你的账单：十分钟起步

把审计方法压缩成一份清单。预期先说诚实：各平台导出格式不同，检查器消费的是标准化的用量事件，你的导出要先过一次字段映射——十分钟只够起步。

1. **导出你的用量数据。** 多数平台支持 CSV 或 API 导出，这是你的数据。
2. **本地跑开源检查器。** conformance pack 在 [github.com/roy-tong/AgentMeasure](https://github.com/roy-tong/AgentMeasure)，MIT 协议，数据不出你的机器。
3. 对着五个家族逐条问：价表覆盖你正在用的模型代际吗？缓存读写乘数按厂商区分了吗？流式重试有没有被双计？缺失字段是不是被 `or 0` 吞了？配额窗口按什么时间锚定？
4. 检查判定是否可追溯。每个判定都应能追到一条具名规则；追不到的按 UNPROVABLE 处理——按 0 处理，等于替对方打折。
5. 用重算结果决定下一步。账单上经得起独立重算的数字，你可以辩护；重算不过的，你手里就有了收据。

检查器背后的结算规范是 [AMS-1](https://github.com/roy-tong/AgentMeasure/blob/main/standard/SETTLEMENT.md)。英文完整版（含逐仓发现索引与复现命令）首发于 [dev.to](https://dev.to/roytong/we-audited-110-ai-usage-tools-here-is-where-the-numbers-go-wrong-5d8h)。
