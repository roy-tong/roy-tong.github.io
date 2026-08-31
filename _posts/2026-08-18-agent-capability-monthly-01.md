---
layout: post
title: "Agent Capability Monthly · Issue 01：生态基线"
subtitle: "创刊号不追求当月新闻，而是把生态的当前状态、计量方法与数据口径固定下来，作为后续每一期的参照。"
date: 2026-08-18 09:00:00 +0800
permalink: /notes/agent-capability-monthly-01/
reading_time: 9
tags:
  - Agent
  - Capability Economy
  - 月度报告
  - 计量
description: Agent Capability Monthly 创刊号。固定八段结构：新能力、新 provider、定价变化、MCP/Skills 生态、Agent 商业、计量进展、Top 5 信号、Roy 的判断。本期刊出生态基线：Capability Index 106 条 / 11 类，以及计量先于支付的现状盘点。
---

> **Agent Capability Monthly** 是每月一期的固定报告，回答一个问题：Agent 作为新的软件消费者，软件经济正在发生什么。结构固定为八段：新能力、新 provider、定价变化、MCP/Skills 生态、Agent 商业、计量进展、Top 5 信号、Roy 的判断。
>
> 创刊号是基线号：不追求当月新闻，而是把生态当前状态、计量方法与数据口径固定下来。后续每一期只报告与基线的变化（delta）。事实标注来源与日期，判断明确标注为判断。

## 0. 为什么现在需要一份月度报告

当软件的消费者从人变成 Agent，旧计量链（安装、席位、页面访问）在每一环断开，而新计量体系还没有形成稳定话语，协议、工具、支付、observability 的讨论是碎片化的。这份报告用固定口径持续记录这个生态，让「变化」可以被看见。

基线的两个事实底座：

- Agent Capability Index（[公共地图](/capability-index/)）：收录 106 条 / 11 类可被 Agent 调用的软件能力，v0.1 种子数据，附 provider、interface、pricing、availability 与来源。
- AgentMeasure（[开放计量基础设施](https://github.com/roy-tong/AgentMeasure)）：五段链 Reach → Choice → Use → Utility → Value，证据分级 E0–E5，观测上下文 Context × 执行有效性 Validity。

## 1. New capabilities 新能力

基线口径：**能力（Capability）= 软件可被 Agent 调用的一次能力，而非整个 App**。收录标准：有公开文档、有可验证的接口（API / CLI / SDK / MCP / 自托管）、能说明计价方式。

基线分布（106 条）：

| 类别 | 数量 | 说明 |
|---|---|---|
| Search 搜索 | 11 | 网页/语义/答案式搜索 |
| Coding 编码 | 10 | 仓库、CI/CD、包生态 |
| Browser 浏览器 | 10 | 自动化、抓取、托管浏览器 |
| Data 数据 | 10 | 文档库、分析库、向量库 |
| Compute 计算 | 11 | 函数、GPU、推理 |
| Communication 通信 | 9 | 消息、邮件、会议 |
| Payments 支付 | 9 | 收单、订阅计费、金融数据 |
| Commerce 商业 | 7 | 电商、卖家后台 |
| Real-world Action 真实世界 | 7 | 配送、出行、预订（多为合作制） |
| Creative Tools 创意 | 10 | 图像、视频、语音 |
| Productivity 生产力 | 12 | 办公、项目管理、文件 |

判断：支付类与真实世界动作类的条目最少、且最不稳定（合作制 API、定价不透明），这正是「计量先于支付」缺口在数据层的体现——越接近钱的能力，越缺少公开口径。

## 2. New providers 新 provider

基线口径：provider = 提供至少一个可调用能力的组织。v0.1 以欧美基础设施厂商为主，中文生态（微信/飞书/钉钉等）将在 v0.2 补齐——这本身就是一个待办，也是社区可贡献的方向（[Add a capability](/capability-index/)）。

判断：当前 provider 结构高度集中在「Agent 时代的基础设施」——搜索、浏览器、向量库、推理 API。真正面向 Agent 的消费级能力（预订、配送、支付）仍以合作制为主，开放度不足。未来 12 个月最值得跟踪的，是真实世界能力开始向 Agent 开放的速度。

## 3. Pricing changes 定价变化

基线事实（来源见链接）：

- 2025 下半年开始的模型定价战持续：Claude Opus 4.5 上市后大幅降价，被视为对 Google 与 OpenAI 的「价格倾销」([reseller.co.nz](https://www.reseller.co.nz/article/4097187/anthropics-claude-opus-4-5-pricing-cut-signals-a-shift-in-the-enterprise-ai-market-3.html)、[PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2025/google-and-anthropic-drop-ai-prices-and-release-new-models/))；o3 价格下调 80%，形成新的性价比档位 ([Towards AI](https://newsletter.towardsai.net/p/tai-157-o3-drops-80-to-undercut-rivals))；Q4 2025 的模型定价变化已被系统性跟踪 ([dataku](https://dataku.ai/blog/every-ai-pricing-change-q4-2025-tracked))。
- 推理成本下降 → Agent 的每次「思考」更便宜 → 单次调用成本占比下降，能力与软件的定价占比上升。

判断：模型价格战是 Agent Capability Economy 的供给侧前提：当推理不再是成本大头，软件的「能力费」才会成为可单独定价、单独计费的对象。这也是 CaaS（Capability as a Service）可能成立的宏观条件。

## 4. MCP / Skills ecosystem 协议与工具生态

基线事实：

- GitHub MCP Registry 上线（2025-09）：为 MCP server 提供集中发现与信任入口 ([InfoWorld](https://www.infoworld.com/article/4061244/github-introduces-registry-for-finding-mcp-servers.html)、[DevOps.com](https://devops.com/github-mcp-registry-launches-as-central-hub-for-ai-development-tools/))。
- MCP 一周年 spec 更新（2025-11）：重点转向授权（authorization）扩展——从「能连」走向「能安全地代表用户调用」([modelcontextprotocol.info](https://modelcontextprotocol.info/blog/first-mcp-anniversary/))。
- 生态规模（站内既有口径）：MCP SDK 月下载量在 2026 年中接近 1 亿次量级；skills.sh 头部 skill 五个月约 200 万次安装。
- 但官方 registry 明确不做采纳与使用数据——发现层在聚合，使用层依然无数据（见第 6 节）。

判断：MCP 生态正在从「协议碎片」走向「协议 + 注册表 + 授权」三层。注册表解决发现，授权解决信任，但两者都不产生使用数据。这意味着：measurement 不是被替代，而是被不断逼近——连接越标准化，计量口径的统一就越可能。

## 5. Agent commerce Agent 交易

基线事实：

- **Agentic Commerce Protocol（ACP）**：OpenAI 与 Stripe 联合推出，为 Agent 代用户购买软件/服务定义协议；Stripe 同步提供 Agent Toolkit（含 paid tools 系统与 usage-based billing/metering）([The AI Journal](https://aijourn.com/agent-commerce-protocol-acp-and-google-ap2-the-next-layer-of-autonomous-transactions/)、[Stactize](https://stactize.com/artikel/stripes-agentic-commerce-protocol-what-it-means-for-saas-companies-selling-through-cloud-marketplaces/)、[DeepWiki: usage-based billing](https://deepwiki.com/stripe/agent-toolkit/4-usage-based-billing-and-metering))。
- Google AP2（Agent Payments Protocol）：与 ACP 并列的自主交易协议候选 ([The AI Journal](https://aijourn.com/agent-commerce-protocol-acp-and-google-ap2-the-next-layer-of-autonomous-transactions/))。
- 站内既有口径：Cloudflare x402 / Agentic Payments、Coinbase Bazaar 与 ACP 同为 2026 年支付层的主要玩家。
- OpenAI DevDay 2025 把 ChatGPT 定位为「AI OS」，in-chat apps 与 commerce 成为平台叙事 ([windowsforum](https://windowsforum.com/threads/openai-devday-2025-chatgpt-as-ai-os-with-in-chat-apps-and-commerce.384079/))。

判断：支付层正在从「谁能收 Agent 的钱」快速收敛为「协议之争」——ACP vs AP2 vs x402 vs Bazaar。但所有支付协议都默认「被计费的使用量是可靠的」。这个默认目前不成立：计量处在链条最前端，行业却把注意力全放在支付那几段上。

## 6. Measurement developments 计量进展

基线事实：

- Stripe Agent Toolkit 直接内置 usage-based billing 与 metering，把「用量计费」做进 Agent 支付栈 ([DeepWiki](https://deepwiki.com/stripe/agent-toolkit/4.2-usage-based-billing-and-metering))。
- OpenTelemetry 发布 AI agent observability 指南，GenAI 语义约定仍在演进 ([opentelemetry.io](https://opentelemetry.io/blog/2025/ai-agent-observability/))。
- 站内既有口径：AAIF 已成立；AgentMeasure 已发布 [Benchmark Run #001]({{ '/notes/every-agent-usage-number-is-self-reported-zh/' | relative_url }})（对六个真实 Agent 用量声明的证据审计：每个数字都是自报的，没人发布单位定义）；CORE 规范到 Draft 0.4.3，Pipeline Validation #001（42 calls → 84 observations）；Measurement Report #001 编号预留给第一个外部 Provider。

判断：计量正在成为「显学」，但方向分化：支付商在做**计量以计费**（metering for billing），可观测工具在做**调试以排障**（observability for debugging），而 AgentMeasure 主张的是第三类——**可验证以比较与结算**（verifiable measurement for markets）。三类目的一致，但口径不同；谁先定义出可验证、跨厂商统一的「Agent 使用量」，谁就拥有下一个 npm 下载量。窗口期就在 2026。

## 7. Top 5 signals 本月最重要信号

1. 协议开始收敛，使用层依然无数据（第 4 节）。
2. 支付商亲自下场做计量：Stripe 内置 metering（第 6 节）。
3. 模型定价战为能力定价铺路（第 3 节）。
4. 真实世界能力开放度不足：Payments 与 Real-world 条目最少且多为合作制（第 1 节）。
5. 标准窗口期：AAIF、OTel GenAI、ACP/AP2 都未定型——2026 年是定义「可验证的 Agent 使用量」的窗口（第 6 节）。

## 8. Roy's updated view 最新判断

基线判断保持不变，并增加一条：

- 不变：measurement 先于 payment；五段链（Reach → Choice → Use → Utility → Value）是不可再压缩的计量粒度；证据分级（E0–E5）是可验证性的最小实现。
- 新增：支付商亲自做 metering 不是威胁，而是验证——它把「计量」从学术主张变成了商业基础设施的组成部分。AgentMeasure 的定位应从「提出计量语言」推进到「成为跨厂商口径的裁判与注册表」：与 ACP/AP2/x402 并存，但不属于任何一家。
- 下一步（8–9 月）：Capability Index 扩到 200+ 条并开放 provider 认领；发布 Measurement Report #001（第一个外部 Provider 数据）；把本刊做成固定预期——每月同日更新。

---

*相关材料：*[Agent Capability Index](/capability-index/) · [当软件的消费者变成 Agent]({{ '/notes/when-the-software-consumer-becomes-an-agent/' | relative_url }}) · [每个 Agent 用量数字，都是自报的]({{ '/notes/every-agent-usage-number-is-self-reported-zh/' | relative_url }}) · [AgentMeasure](https://github.com/roy-tong/AgentMeasure) · [订阅 RSS](/feed.xml)
