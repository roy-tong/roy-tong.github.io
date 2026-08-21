---
layout: post
title: "AI 应用不会被 Agent 塞满，它们会先被拆掉"
subtitle: "从 DSH 与 Codex Harness 看：软件的基本单位正在从 App 变成一次运行时组合。"
date: 2026-08-21 10:00:00 +0800
reading_time: 15
tags:
  - Agent
  - Harness
  - Capability Economy
  - SaaS
  - Ephemeral Software
description: 把 DeepSeek Harness 和 Codex Harness 放在一起看，会发现一条比"给软件加 Agent"更激进的路线：模型、Skill、工具、数据、执行环境和界面在运行时临时组合，任务结束后随之消失。软件的基本单位正在从 App 变成 Capability，SaaS 会被拆包，商业模式从 Seat Economy 转向 Machine Economy。
---

过去一年，AI 应用最常见的产品思路，是给现有软件加一个 Agent：CRM 加销售 Agent，文档工具加写作 Agent，设计软件加创作 Agent。

把 DeepSeek Harness（DSH）和 Codex Harness 放在一起看，会看到另一条更激进的路线：未来的软件未必还是一个封装好的 App。模型、Skill、工具、数据、执行环境和界面可以在运行时临时组合，任务结束后，这套组合也可以随之消失。

今天我们打开一个个 App。以后，Agent 可能根据任务临时组装一个"应用"。

这不是给旧软件多装一个聊天框，而是在改变软件的基本单位。

## Harness 正在变成新的软件运行时

DeepSeek 对 Agent 的定义很直接：

> Agent = Model + Harness

DSH 把模型、工具、Skill、会话、沙箱、存储、Loop、调度和 UI 都做成插件。标准模式、PTC 模式、极简模式和创造模式，背后是不同的运行时组合。创造模式甚至可以检查当前 runtime、在内存中试验插件，再把它们组合成新的 preset。[DeepSeek 官方预览页](https://deepseek.com/harness/)

Codex 走的路径不同，落点却很接近。Codex 的 Web、CLI、IDE 扩展和桌面 App 共用同一套 Harness；App Server 通过双向 JSON-RPC，把 Agent Loop、会话、配置、授权和事件流暴露给不同客户端。外部产品也可以借此嵌入 Codex，而不用重新实现整套 Agent 逻辑。[OpenAI：Unlocking the Codex harness](https://openai.com/index/unlocking-the-codex-harness/)

两家公司都在做同一件事：把 Harness 从产品内部的实现细节，变成可复用、可组合的运行时。

DSH 仍处于开发者预览阶段，官方也明确提醒核心插件和 API 还会变化。Codex App Server 同样是快速演进中的平台接口。它们还不是已经定型的行业标准，但方向已经足够清楚。

## App 会变成一次运行时组合

传统软件把界面、流程、业务逻辑、数据和执行能力打包在一起：

```text
用户 → App → UI / Workflow / Logic / Data / Execution
```

Harness-native 软件更像：

```text
用户目标
   ↓
Agent
   ↓
Harness
   ↓
按任务选择 Model / Skill / Tool / Data / UI
   ↓
执行并交付结果
```

比如用户提出一个任务：

> 研究大疆最近两年的海外市场变化，给我一份带图表的报告。

Harness 可以临时加载网页搜索、财务数据、视频与论坛检索、PDF 阅读、电子表格、图表生成和报告渲染。它们共同组成一个研究应用。报告交付后，这个组合没有必要继续存在。

这类软件可以叫 Ephemeral Software：为一个任务生成，运行一次或几次，然后消失。

软件不会因此变少。恰恰相反，当开发和组装成本下降，大量过去不值得单独开发的内部工具、个人工具和一次性工具都会出现。减少的可能不是软件数量，而是每一份软件都要变成长期产品的必要性。

## SaaS 会被拆包，Workflow 最先承压

今天的 SaaS 通常把五层东西一起卖给用户：

| 层 | SaaS 提供的内容 |
| --- | --- |
| Interface | GUI |
| Workflow | 固定流程 |
| Logic | 业务规则 |
| Data | 业务数据 |
| Execution | 执行动作 |

Agent 最容易接管的是 Interface 和 Workflow，因为自然语言正在成为新的交互入口，Harness 又能负责流程编排。

过去，销售要进入 CRM，筛客户、查记录、写邮件、建任务、设 follow-up。以后，他只需要说：

> 找出过去两周没有跟进、但成交概率最高的 20 个客户。分别写一封邮件，高价值客户先让我确认。

CRM 的大量页面和点击路径会退到 Agent 背后，但客户记录、权限、历史互动、邮件发送和审计日志不会消失。Agent 越能执行任务，越需要这些真实数据和动作接口。

所以 SaaS 面临的不是整齐划一的"死亡"。分化会更明显：

- 靠用户手动操作固定流程创造价值的 Workflow SaaS，风险更高。
- 掌握业务事实的 System of Record，价值可能上升。
- 能完成真实动作的 System of Action，也会变得更重要。

判断一家软件公司是否安全，可以问一个很直接的问题：

> Agent 有没有理由绕过它？

如果 Agent 只需要它的 API，不需要它的界面，产品的定价、分发和护城河都要重新算。

## 软件市场会从 App Economy 转向 Capability Economy

今天，软件行业的基本单位是 Application：Photoshop、Figma、Salesforce、Expedia。

Harness 看到的却是一个个能力：

```text
remove_background()
render_video()
query_customer()
book_flight()
generate_contract()
send_campaign()
```

应用被拆开后，Agent 要做的是在任务中发现、比较和调用能力。DSH 的插件架构已经把这件事推进到运行时内部；它的 subagent 接口还允许同一上下文注册多个 provider，包括 Codex、Claude Code 和 DSH SDK。[DeepSeek Harness：Subagent](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/subagent.md)

Agent 也开始成为另一个 Agent 的 Tool。软件生态不再只是 App Store 里的一排图标，而会逐渐长成一张 Capability Graph：通用 Agent 负责理解目标，专业 Agent 接下子任务，再调用底层工具和服务。

新的分发问题也随之出现。开发者过去研究的是"怎么让人下载我的 App"，以后还要研究"怎么让 Agent 选择我的能力"。

这会催生新的基础设施：Capability Registry、Agent Search、可靠性排名、Eval、归因、支付和声誉系统。

## 模型很重要，但模型优势不等于应用壁垒

当模型和 Harness 解耦，同一套运行时可以接多个模型：分类交给小模型，代码交给 Coding Model，视觉任务交给 VLM，复杂推理再调用 Frontier Model。

顶级模型仍然有巨大的价值，只是应用不必把全部能力押在单一模型上。Harness 越成熟，应用越容易根据成本、速度和任务类型切换模型。

这会让一批"LLM API + Prompt + Workflow + 漂亮 UI"的应用承压。Agent Loop、工具调用、上下文管理、沙箱、权限、Skill 和 Subagent 正在变成公共基础设施。单纯把这些部件拼在一起，越来越难形成长期壁垒。

## AI 应用的壁垒会集中到五种资产

Harness 可以复制工作流，却不能凭空生成真实世界里的资产。未来更值得看的，是下面五件事：

1. 独有的 Context 和 Data：客户记录、案件材料、库存、价格、历史交互。
2. Execution：支付、发货、发邮件、改配置、提交订单等真实动作。
3. Feedback Loop：大量任务结果能否持续改善判断和执行。
4. Permission 和 Trust：用户是否敢授权它处理资金、隐私和高风险操作。
5. Distribution 和 Network：用户、商家、开发者和供需关系是否已经形成网络。

法律 Agent 的价值不会来自一个"很懂法律"的 Prompt，而会来自案例库、客户材料、执业权限、律师网络和案件结果。

电商 Agent 也一样。推荐话术容易复制，商品、库存、价格、支付、物流和售后网络复制起来很慢。

企业 AI 的护城河则会落在企业数据、权限、执行接口、审计和历史结果上。

## 代码会变便宜，"什么叫正确"会变贵

OpenAI 的 Harness Engineering 实验提供了一个很具体的信号：一个内部 beta 项目的代码库在五个月后达到约百万行，覆盖应用逻辑、基础设施、工具和文档；期间约有 1,500 个 PR 被创建并合并，起初由三名工程师驱动 Codex 完成。[OpenAI：Harness engineering](https://openai.com/index/harness-engineering/)

OpenAI 对这项实验的总结不是"程序员消失了"。团队的主要工作从亲手写代码，转向设计环境、表达意图和建立反馈闭环。

代码生成得越快，真正稀缺的东西越往上游移动：

```text
Specification
Architecture
Test
Eval
Policy
Context
Observability
Feedback Loop
```

实现成本下降，不代表软件工程变简单。工程师要把"正确"写进环境，让 Agent 能检查、修正并持续运行。Harness Engineering 这个名字准确地描述了这种变化。

## GUI 不会消失，它会变成 Control Plane

所有软件都变成聊天框，既不现实，也没有必要。

视频时间线、3D 空间、CAD、地图和设计画布依然是高带宽输入工具。Agent 完成任务后，人也需要检查、比较、修改和确认结果。

GUI 更大的变化，是操作层逐渐让位给控制层：

- Agent 正在做什么？
- 它用了哪些数据？
- 花了多少钱？
- 为什么做这个决定？
- 哪些动作需要批准？
- 失败发生在哪里？

工作台不会消失，但它的重心会从 Workspace 移向 Control Plane。

## 商业模式会从 Seat Economy 转向 Machine Economy

SaaS 按 seat 收费，是因为人在操作软件。Agent 成为主要操作者后，一个 Agent 可能替代大量页面操作，同时产生远高于人的 API 调用量。

计价方式会逐渐向 Usage、Transaction、Outcome、Compute、Data 和 Agent Action 移动。

这不一定降低 SaaS 的收入。一个人一天打开 CRM 20 次，一个 Agent 可能调用接口 20,000 次。软件消费没有消失，消费者从人变成了机器，定价单位也要跟着变。

## 接下来值得关注的五个位置

未来三到五年，最有机会的可能不是另一个 Chat UI，而是五个基础位置：

- Agent Runtime / Harness Infrastructure：让 Agent 长期稳定运行。
- Context Infrastructure：让 Agent 获得正确、可更新的长期上下文。
- Capability Economy Infrastructure：帮助 Agent 发现、购买和调用服务。
- Trust / Eval / Observability：判断 Agent 和 Tool 是否可靠。
- Vertical System of Action：控制行业数据、执行能力和反馈闭环，直接交付结果。

最后一类的市场可能最大。AI 招聘、法务、财务、电商运营、市场研究、软件开发、内容生产和客服，最终比拼的都不是"谁做了一个行业 Agent"，而是谁掌握了 Agent 完成任务时绕不开的数据、权限、动作和结果。

## 软件的第一用户，正在从人变成 Agent

过去，人是用户，软件是工具。

现在，人还是用户，Agent 是助手，软件继续当工具。

再往前走一步，人只负责提出目标，Agent 会成为软件的直接使用者：

```text
Human → Goal → Agent → consume Software
```

这才是 DSH 和 Codex Harness 释放出的真正信号。Coding Agent 变强只是表面变化，底层变化是"Agent 作为软件第一用户"的基础设施开始成熟。

Harness 会把 Agent 平台化，Agent 会吸收大量 Workflow。传统 App 随后被拆成 Experience、Context、Capability 和 Execution。

以后最有价值的软件公司，未必拥有界面最完整的 App。它可能只拥有一项能力，但那项能力掌握真实数据、可以执行关键动作，而且 Agent 无法绕开。
