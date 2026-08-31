---
title: "Agent 计量：执行事实、任务结果与价值"
topic: agent-systems
order: 30
reviewed_at: 2026-08-31
summary: "明确分母和证据边界，避免把重试、调用成功、被使用和业务收益混成一个数字。"
related: ["software-capabilities","demand-evidence","evidence-maintenance"]
related_posts: ["/notes/agent-usage-measurement-standard/","/notes/agentmeasure-from-spec-to-evidence/","/notes/every-agent-usage-number-is-self-reported-zh/"]
source_ids: ["agentmeasure-core","agentmeasure-evidence","agentmeasure-lab"]
---

AgentMeasure 研究的问题很具体：软件被 Agent 调用以后，怎样描述发生了什么，并让别人检查数字的含义。它仍是开放草案与实现项目，不是已经被全行业采纳的计量标准。

## 同一件事，不能混用分母

一个演示例子：用户要求生成一次报告，服务端第一次尝试失败，第二次成功。若两次尝试确实属于同一个逻辑操作，应记录：

| 指标 | 结果 | 分母 |
| --- | ---: | --- |
| attempts | 2 | 实际执行尝试 |
| operations | 1 | 去重后的逻辑操作 |
| attempt success | 50% | 成功尝试 / 全部尝试 |
| operation success | 100% | 成功操作 / 全部操作 |

这只是解释语义的例子，不是生产测量结果。若日志缺少操作标识，无法可靠关联重试，就必须披露归组规则和未知部分，不能强行凑出一个精确操作数。

## 一条测量链有多处断点

“可用 → 被展示 → 被选择 → 执行 → 有用 → 增量价值”中，每个箭头都需要证据。服务端日志擅长描述执行，未必知道 Agent 看到了哪些备选项；客户端选择记录也未必知道最终用户是否接受结果。

测量报告应该先写可观察范围，再给指标。没有展示分母，就不报告选择率；没有用户验收，就不把 HTTP 成功等同于任务成功；没有可比较的对照，就不把前后增长写成因果收益。

## 怎样读当前项目的证据

[公开 trace 案例](https://github.com/roy-tong/AgentMeasure/tree/main/conformance/evidence/langfuse-demo-traces)用于检查适配、字段和计数边界。它来自演示数据，不能替代真实客户生产流量。

[Lab](https://github.com/roy-tong/AgentMeasure/tree/main/lab)提供预注册、实验组织和报告工具。随附合成实验用于验证引擎能否恢复已知效应，也能报告没有效应的结果；不说明真实 Agent 已获得同样提升。

这种限制应出现在结果附近，不能藏在文末。

## 计费还需要另一份契约

业务可以按尝试、成功操作、时间或结果收费，但需要预先定义失败、重试、取消、超时和人工接管如何处理。计量准确不等于价格合理；收到付款也不等于创造了增量价值。

我会把下一阶段验证放在真实日志中无法归组的操作、没有回传的最终结果，以及不同工具之间不可比的成功口径。一个让原有数字变得不那么漂亮、却更容易检查的测量系统，仍然有价值。
