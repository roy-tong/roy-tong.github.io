---
layout: post
title: "AgentMeasure 一周进展：规范开始长出证据"
subtitle: "v0.2.0 → v0.2.2：实验引擎、真实 Agent 上的 A/B、首个外部 fixture、首个公开证据案例，以及一次 0% 的诚实报告。"
date: 2026-08-25 14:20:00 +0800
permalink: /notes/agentmeasure-from-spec-to-evidence/
reading_time: 5
tags:
  - Agent
  - Capability Economy
  - 计量
  - 进展周报
description: "AgentMeasure 近一周（8/22–8/25）的工程与证据进展：Lab v0.4 开源实验引擎、codex 真实 Agent 上的首个预注册 A/B、v0.2.2 一致性加固（首个外部 fixture Urusilla-001）、首个公开证据案例（langfuse demo traces：12 次尝试、安全操作覆盖率 0%），以及规范从「阶梯」到「两状态 + 分级证据」的修订。"
---

> 这是 AgentMeasure 的第一篇进展周报。项目主页：[github.com/roy-tong/AgentMeasure](https://github.com/roy-tong/AgentMeasure)，官网：[roy-tong.github.io/AgentMeasure](https://roy-tong.github.io/AgentMeasure/)。以下所有数字都来自可复现的运行输出，不含手抄转写。

## 一周做了什么

过去一周，项目从「规范文档」推进到「证据飞轮」。四个版本节点，一条主线：每一条声明都要能被复算。

**v0.2.0（8/22）**——白皮书 v0.3（中英双语）+ AgentMeasure Lab v0.4 开源实验引擎：预注册（preregistration）锁、均衡分组、预算熔断、诚实统计（Wilson 区间、双比例检验、诚实零结果），以及面向决策者的双语一页纸报告。78 个测试。

**v0.2.1（8/22）**——在真实 Agent 上跑通了第一个预注册对照实验（codex CLI + 真实 MCP 工具服务器）：4 任务 × 2 变体，全漏斗采集，真实 token 计量（每个操作 188K–215K tokens）。结果是一个零结论：观测到 +25pp 但 p=0.29，下一轮需要约 31/臂。引擎没有美化它，这正是引擎存在的意义。

**v0.2.2（8/24）**——一致性加固。第一轮外部一致性测试（来自 [langfuse 讨论 #16383](https://github.com/langfuse/langfuse/discussions/16383)）暴露了两个真 bug：校验器在 `oneOf` 匹配后跳过根级必填字段（#8）；聚合器信任声明的操作摘要而不核对底层的尝试行（#9）。两者都已修复，并且——按当时的承诺——第一个外部贡献的 fixture（Urusilla-001）被接受进一致性套件。CI 现在每次都跑外部 fixture 门禁 + Lab 全套测试。

**8/25**——第一个公开证据案例发布（`conformance/evidence/langfuse-demo-traces/`）：把 Langfuse 公开的 demo 种子数据（三条真实框架遥测 trace，commit 锁定、源不分发）通过一次性适配器跑过规范管线。结论是一个 0%：

- 12 次 attempts，操作分组证据 **100% 缺失**；
- **安全操作覆盖率 0%**（fail-closed 与 structural-experimental 两种模式下都是）；
- token 用量在导出中整体缺席（0/26）。

这个案例把 claim boundary 钉死：这些数字只描述这三条 trace。可复现脚本（`fetch_source.py` + `run_case.py`，纯标准库）随案例发布，任何人可以复算。

## 规范的修订：从阶梯到两状态

同一周，两位独立的外部评审人（经私信交流，匿名待授权）在阅读规范后独立收敛到了同一个批评：我原来设计的四级消费阶梯里，`referenced`（被引用）不是一个语义状态，而只是一个对 influence 的弱估计器，它有两种具名失败模式——**引用了但没用**（cite-without-use）和**用了但没引用**（use-without-cite）。

规范因此修订为 DR-005「两状态 + 分级证据」：

- **availability**（上下文事实）：能力是否进入了 Agent 的上下文；
- **influence**（行为事实）：能力是否改变了 Agent 的行为——由实验层回答。

另一位评审人补上了 provider 侧的推理边界：客户端遥测能证明的是 `serialized-as-sent`（已序列化发出），离 `reached-inference`（到达推理）还差一步。这个边界现在写进了定义。

同时发布的还有 DR-006 落地的 **M3 执行粒度向量**：一条运行时重试链（429 → timeout → success，同一个 `operation_id`）在规范里归为 1 次操作，M3.3 尝试成功率 0.333，`attempts_per_operation = 3` 强制披露——而不是把三次技术调用计成三次「使用」。两名专家独立收敛到同一个批评，事后看是对规范方向的一次行为验证。

## 产品与增长的现实

同期发布的 [PRD v0.5](https://github.com/roy-tong/AgentMeasure) 记录了双假设并行受试：A（一致性工具箱，已有真实外部拉力）对 B（用量完整性审计，离钱近但未验证），9/3 做 gate review。

一个已经被证伪的渠道：冷邮件。616 封送达 → 1 封有意义的回复 → 0 次集成。这条渠道已关闭。

一个被验证的回路：**上游结构化参与**。从 langfuse 的一个 issue 出发 → 第一轮外部一致性测试 → 抓出 #8/#9 两个真 bug → 修复并发布 v0.2.2 → 第一位外部贡献者提交 fixture。这条「参与 → 证据 → 修复 → 贡献」的回路，是本周进展里最有分量的一条。

官网（[roy-tong.github.io/AgentMeasure](https://roy-tong.github.io/AgentMeasure/)）的 Trial 入口也改成了双路径：邮件直达优先，GitHub issue 降为次选——审计的目标人群是 CEO/CFO，不该逼他们开 GitHub 账号。

## 下一步

- 9/3：双假设 gate review（四分支裁决标准已预注册）；
- Lab M2 开源发布与一致性向量补齐（Execution / Reporting 层）；
- 复制「上游结构化参与」回路到下一批 observability / gateway / runtime 项目；
- Show HN 的四个 gate 已过三，只差一段 2 分钟 demo。

一句话总结这一周：标准不再只是一份文档，它开始产出自己的证据。
