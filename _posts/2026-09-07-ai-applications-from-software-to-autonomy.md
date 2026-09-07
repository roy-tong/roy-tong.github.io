---
layout: post
title: "AI 应用的下一站，不是更多 Agent"
subtitle: "当模型越来越通用，应用的价值正在从能力与工具，迁移到工作、结果、交易与现实世界的自主闭环。"
date: 2026-09-07 11:30:00 +0800
lang: zh-CN
reading_time: 20
tags: ["AI 应用","Agent","AI Native Service","具身智能","世界模型","产业判断"]
description: "从近期 VC 对 AI 应用、Infra、Result-as-a-Service 的判断出发，结合 Coding、客服、医疗等已经跑通的范式，以及通用 Agent、世界模型、Physical AI 与 BCI 的演化，重新回答一个问题：基础模型持续变强之后，什么样的 AI 应用会被吞掉，什么样的公司反而会越来越值钱？"
permalink: /notes/ai-applications-from-software-to-autonomy/
knowledge_topic: agent-systems
knowledge_units: ["software-capabilities","agent-context","world-models","robot-industry"]
---

最近和一些投资人聊 AI 应用，得到的反馈有点互相打架。

一边是，底层 Infra 的故事越来越难讲。Agent 还没有出现足够大的杀手级应用，支付、身份、Eval、Memory、Observability 等基础设施，即使方向正确，也会被追问一个很现实的问题：下游到底有多少真实 workload？支付宝可以很重要，但支付宝的价值并不是凭空长出来的，它后面先有淘宝和交易。

另一边是，资本又开始重新看 AI 应用，尤其是那些人力密集的行业。逻辑不再是做一个更聪明的工具，而是直接接掉一部分人的工作，甚至交付最终业务结果。过去卖 SaaS，未来可能卖 Result-as-a-Service。

同时，还有一个始终绕不开的问题：基础模型一直在进步。去年我自己创业，以及后来在大疆做 Video Agent 时，都遇到过同一类困境。很多当时看起来需要专用 Agent 才能完成的事情，随着 Claude Code、Codex 一类通用 Agent 变强，专属产品的空间会迅速被压缩。

再往另一边看，越来越多最顶尖的 AI 研究者和创业者又在进入世界模型、具身智能、机器人和脑机接口。看起来像是数字世界卷到一定程度之后，AI 正在寻找进入现实世界的新出口。

这些观点单独看都有道理，但放在一起容易得到几种彼此矛盾的结论：

- AI 应用会重新繁荣；
- 通用 Agent 会吞掉大量 AI 应用；
- AI Infra 价值很大，但现在又不好成立；
- Result-as-a-Service 是下一波机会；
- 真正长期的机会又可能在 Physical AI；
- 模型越来越强，到底是在帮助应用，还是消灭应用？

我现在更倾向于换一个问题。

**不要再问“AI 应用是什么”，而要问：机器正在接管哪一层责任？**

这条责任边界的移动，比 Agent、Infra、机器人这些品类词更能解释下一阶段的产业变化。

## 一、AI 的真正演化轴：从生成能力，到承担责任

过去三年的 AI 产品，大致经历了五个层级。

| 层级 | AI 做什么 | 人承担什么 | 客户真正购买什么 |
| --- | --- | --- | --- |
| Capability | 生成文字、图片、代码、视频 | 判断、组织、执行 | 一项能力 |
| Copilot | 辅助一个岗位工作 | 决策和最终执行 | 效率提升 |
| Agent | 独立完成一个任务 | 提目标、审批异常 | 完成任务 |
| Operator / Service | 接管一段完整工作流 | 管理例外与责任边界 | 业务结果 |
| Autonomous System | 持续感知、决策、行动并自我修正 | 定义目标与边界 | 持续运行的产能 |

ChatGPT 最初解决的是“给我一个答案”。

Copilot 解决的是“帮我把这件事做快一点”。

Agent 开始变成“这件事你替我做”。

Result-as-a-Service 再往前一步：“我不关心你怎么做，我只买结果。”

机器人、自动驾驶、工业自治系统则把责任继续扩张到物理世界：机器不只是修改文件和数据库，而是持续改变现实状态，并为这些状态变化承担可靠性要求。

所以更底层的演化不是：

> Chatbot → Agent → Robot

而是：

> **Information → Decision → Action → Outcome → Autonomy**

AI 每往前走一步，都是把过去必须由人承担的一部分责任，转移给机器。

这条线能解释为什么很多 AI 产品会迅速消失，也能解释为什么另一些公司会因为模型变强而越来越大。

## 二、应用层重新变重要，不代表 Wrapper 又有机会了

2025 年，美国企业在生成式 AI 上的支出约 370 亿美元，其中应用层约 190 亿美元，已经超过一半。Coding 单一品类约 40 亿美元，占部门级 AI 支出的 55%；Vertical AI 约 35 亿美元，其中医疗约 15 亿美元。Menlo Ventures 把 Coding 称为第一个真正跑出来的 killer use case。[Menlo Ventures, 2025 State of Generative AI in the Enterprise](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)

这组数字说明应用层确实在重新获得价值，但不能把它理解成“模型之上的 App 又重新安全了”。

真正变化的是，应用正在分成两个物种。

第一种，我称为 **Capability Application**。

它卖的是 AI 本身会做什么：写作、总结、翻译、生成 PPT、剪视频、搜索、画图、写代码。

这类产品的问题是，它的核心产品价值往往就是基础模型当前还没有完全提供的那一截能力。模型一旦补齐，这一截差异就消失。

第二种是 **Responsibility Application**。

它卖的不是“AI 会什么”，而是“这件事情最后有没有完成”。

例如：

- 客诉有没有解决；
- 理赔有没有关闭；
- 欠款有没有收回来；
- 合同有没有完成审阅并进入签署；
- 病历、编码、支付链路有没有处理完；
- 代码有没有通过测试并成功部署。

后者的核心价值并不依赖模型保持缺陷。恰恰相反，模型越强，它能承担的责任范围越大。

这是两类应用最本质的差异。

## 三、判断一个 AI 项目，先做“模型十倍测试”

假设明天基础模型能力提升十倍，成本再下降一个数量级，会发生什么？

如果结果是：

> 用户直接用基础模型就行，不需要这个产品了。

这是典型的负模型梯度。

如果结果是：

> 产品可以自动完成更多工作、减少更多人工、进入更多复杂场景、提高毛利率。

这是正模型梯度。

可以把它叫作 **Base Model Acceleration Test**。

| 模型能力提升 10 倍之后 | 项目状态 |
| --- | --- |
| 产品核心功能被模型原生覆盖 | 高风险 |
| 体验更好，但差异化快速缩小 | 偏风险 |
| 自动化率从 30% 提升到 60% | 好 |
| 人工 Exception 大幅下降 | 很好 |
| 能从单点任务扩到完整 Workflow | 很好 |
| 能开始直接对 Outcome 收费 | 更好 |
| 能进入交易、资金或资产流 | 最强 |

这也是我现在重新理解 Video Agent 的方式。

如果一个 Video Agent 的价值链只是：

> 理解意图 → 规划剪辑 → 调用视频工具 → 生成成片

那么通用模型和通用 Agent 变强，会不断向下覆盖它。过去必须自己做的 planning、tool use、multimodal understanding，都会逐渐成为公共能力。

但如果继续往下走：

> 内容生产 → 投放 → 受众测试 → 迭代素材 → 转化优化 → 对 GMV 或 ROI 负责

它就不再只是 Video Agent，而开始变成一个业务 Operator。模型越强，它单位内容的生产成本越低，能够尝试的创意越多，闭环越快。

这就是“吃模型红利”和“被模型替代”之间真正的分界。

**好的应用不应该建立在模型永远做不到某件事上，而应该建立在模型越能做事，我能接管越多责任上。**

## 四、为什么 Coding 是目前最值得迁移的成功范式

如果要从已经跑通的领域寻找规律，Coding 比绝大多数 AI 创业案例更值得研究。

原因不是程序员更愿意尝鲜，而是代码世界几乎天然适合 Agent。

它同时满足几个条件：

1. 输入高度数字化：代码、Issue、文档、Git History 都天然机器可读；
2. Action Space 清晰：编辑文件、运行命令、调用工具；
3. 结果可以验证：Compile、Test、Benchmark、Diff；
4. 环境可以 Reset：Git 可以回滚，Sandbox 可以重建；
5. 人力成本高：同样自动化率对应很高的经济价值；
6. 模型进步直接扩大任务边界：从补全一行代码，到改一个文件，再到处理 Repository-level Task。

因此 Coding 的产品演化不是：

> 模型会写代码了 → Coding 产品消失

而是：

> Autocomplete → Chat → Edit → Agent → Repository Task → PR → SDLC

模型越强，应用接管的 Workflow 越长。

这才是应该迁移的“成功范式”。不是照抄一个 Coding Agent 的产品形态，而是寻找其他行业里同样具备 **数字输入、清晰动作、可验证结果、昂贵劳动、低成本重试** 的工作。

反过来，“人力密集”本身并不够。

很多人力工作并不适合 AI：输入在人的脑子里、环境高度非结构化、结果半年后才知道、一次错误就造成巨额损失，或者大量价值来自关系和责任背书而不是任务执行。

所以更准确的筛选公式应该是：

> **Digitality × Repeatability × Verifiability × Actionability × Economic Density**

五项同时高，才更接近下一批 AI Native Service 的沃土。

## 五、Result-as-a-Service 不是换一种收费，而是软件开始吞服务业

Bessemer 在 2026 年 7 月把这一趋势定义为 **Owning the Outcome**：过去软件帮助专业服务公司工作，现在 AI 可以进入服务交付本身，直接交付完成后的合同、理赔、报告或业务结果。[Bessemer Venture Partners, Owning the Outcome](https://www.bvp.com/atlas/owning-the-outcome-bessemers-ai-native-services-evaluation-framework)

这件事重要，不是因为 SaaS 从 Seat Pricing 改成了 Outcome Pricing。

真正的变化是 TAM 的定义变了。

传统 SaaS 争夺的是 Software Budget：

> 一家公司有 100 个员工，每人每月 50 美元。

AI Native Service 争夺的是 Labor / Outsourcing / Professional Service Budget：

> 你原来每年花 1000 万雇人和外包完成这项业务，我以 300 万完成其中 70%。

客户得到成本下降，AI 公司获得的软件收入却可以远高于传统 Seat 模式。

这不是 SaaS 的一次产品升级，而是软件第一次开始直接进入服务业的生产函数。

客服已经出现很明确的先行信号。Intercom 的 Fin 按 Outcome 收费，一个成功 Resolution 才计费；Salesforce 2026 年推出的 Help Agent 也采用 Pay-per-Resolution，未解决或升级人工的 Session 不计为成功结果。[Intercom: Fin AI Agent Outcomes](https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes)；[Salesforce: Help Agent Resolutions](https://help.salesforce.com/s/articleView?id=ai.usage_flex_credits.htm&language=en_US&type=5)

收费方式之所以值得看，是因为它反映了产品责任的变化：

> 从“我给你一套工具”，变成“我为完成负责”。

未来很可能会看到更多公司表面上不像软件公司，而像律所、会计公司、客服外包、招聘公司、保险 TPA、医疗运营服务商。区别只在于它们内部的生产方式变了：大部分标准工作由 Agent 完成，人处理异常和高责任场景。

这类公司的产品，不只是一个 Agent 界面，而是整套 AI Native Organization。

## 六、真正的 AI Native 公司，核心不是 Agent，而是“异常率曲线”

Result-as-a-Service 很容易被讲成一句漂亮的话，但真正决定商业模型的，是另外一个指标：

> **每完成 100 个任务，需要多少次人工介入？**

如果每个任务都要人复核，AI 只是提高员工效率，公司仍然是传统服务业。

如果 100 个任务只需要人处理 30 个异常，已经开始改变人效。

如果模型持续变强后变成 10 个、3 个、1 个，公司的成本结构会发生质变。

所以 AI Native Service 最重要的经营曲线不是 DAU，也不只是 Token Cost，而是：

> **Human Exception Rate ↓**

以及由此带来的：

> Automation Rate ↑ → Gross Margin ↑ → Addressable Workflow ↑

这也是为什么很多 AI 公司最终必须自己做 Eval、Tracing、Feedback、Human Review 和数据闭环。这些看起来像 Infra 的东西，在一个真正交付业务结果的公司里，不再是附属工具，而是生产系统。

## 七、这也解释了为什么 Infra 的故事现在变难了

Infra 没有变得不重要。

恰恰相反，AI 越承担责任，越需要：

- Eval；
- Observability；
- Identity；
- Permission；
- Memory；
- Payment；
- Security；
- Audit；
- Settlement。

问题只是价值出现的顺序。

在 workload 还很小的时候，先做一个“Agent 支付协议”“Agent 身份网络”“Agent 结算层”，很容易陷入等待市场的问题。

基础设施真正强势的路径，往往是：

> **先有大量真实业务 → 内部长出基础设施 → 基础设施形成行业标准 → 再独立平台化。**

而不是：

> 先造一个基础设施 → 等待未来所有 Agent 来调用。

淘宝和支付宝的类比就在这里。支付基础设施当然重要，但它的早期价值来自真实交易密度，而不是“支付这个方向长期一定重要”。

因此今天做 AI Infra，除了技术问题，还必须回答一个业务问题：

> **我依附的哪条 Agent workload 正在快速增长？**

没有下游 workload，Infra 是期权；有了高频业务流，它才变成控制点。

更现实的一条创业路径，可能是 **Application → Internal Infra → Platform**，而不是反过来。

## 八、通用 Agent 会吞掉大量 App，但未必吞掉 Business

另一个容易走极端的判断是：Codex、Claude、豆包、千问这类通用 Agent 越来越强，未来所有垂直 Agent 都会消失。

我同意前半句，不同意后半句。

通用 Agent 最容易吞掉的是：

- GUI；
- 固定 Workflow；
- Prompt 工程；
- 通用 Planning；
- 普通 Tool Routing；
- 缺乏专有 Context 的单点能力。

也就是说，它会快速压缩大量“AI 产品壳”的空间。

但 Business 还有另外几层东西：

> Context、Permission、Domain Data、Operations、Compliance、Evaluation、Liability、Distribution、Transaction。

例如未来用户完全可能不再打开一个保险理赔 App，只对通用 Agent 说：

> 帮我处理这次事故。

通用 Agent 再调用背后的理赔 Operator。

于是 UI 被吞了，但理赔业务没有消失。

软件从 Human-facing App 变成 Agent-callable Capability，甚至进一步变成 Agent-callable Business。

所以未来的结构可能不是一个超级 Agent 吞掉整个软件产业，而是：

```text
Foundation Intelligence
        ↓
General Agent / Runtime
        ↓
Identity + Context + Permission
        ↓
Vertical Operator / Service
        ↓
Outcome
        ↓
Transaction
```

最上面的入口可能高度集中，下面的经济活动未必集中。

**Agent 会重做分发，不等于它会拥有所有产业利润。**

## 九、模型越强，护城河反而越往模型之外迁移

当模型本身不断商品化，应用的护城河不会消失，而会迁移。

过去大家喜欢讲 Proprietary Model。

下一阶段更值得看的可能是：

### 1. Context

企业数据、用户历史、业务状态、长期 Memory。

### 2. Permission

系统到底有权执行到哪一步，谁审批，什么动作可逆，什么动作必须转人工。

### 3. Workflow Ownership

不是知道怎么做，而是真的处在业务链路里。

### 4. Eval / Verification

结果究竟有没有完成，完成得对不对，如何追责。

### 5. Operations

异常处理、人工兜底、客户交付、复杂长尾。

### 6. Distribution

谁能持续获得真实任务，而不是一次体验流量。

### 7. Regulation / Liability

金融、医疗、法律、工业等领域，谁能承担合规与责任。

### 8. Transaction Network

一旦产品进入资金、订单、资源分配和撮合，价值捕获会再上一个台阶。

这些东西有一个共同特征：

> **模型越强，它们越有用，而不是越没用。**

一个好公司应该是 Model-leveraged，而不是 Model-dependent。

## 十、Abridge 给了另一种很值得看的演化：从 Wedge 到 Workflow

医疗 Ambient Scribe 一开始看起来很像一个容易被模型吃掉的功能：听医生和患者谈话，然后生成病历。

如果产品永远停在“语音转结构化文本”，长期确实危险。

但 Abridge 的演化方向不是把 Scribe 做得更花哨，而是继续进入医疗工作流。2026 年 6 月它发布新的 clinician intelligence platform，把临床对话进一步连接到 care delivery、payment 和 evidence-based treatment；8 月又宣布其 context-aware clinical intelligence 已被 300 多家医疗系统采用。[Abridge, June 2026](https://www.abridge.com/press-release/patient-centered-clinician-intelligence-platform-keynote)；[Abridge, August 2026](https://www.abridge.com/press-release/context-aware-clinical-intelligence-extended-to-all-partners)

这条路径很典型：

> **Point Capability → Workflow → System of Action → Business Outcome**

很多今天成功的 AI 应用，真正值得迁移的不是第一版产品，而是这个向下扎的过程。

一个 Narrow Wedge 只是获取真实场景、Context、数据和分发的入口。真正的公司价值来自它能不能沿着业务链继续扩大责任范围。

## 十一、Physical AI 不是 Agent 的“下一站”，而是另一条并行的责任扩张

再看世界模型、具身智能和机器人。

很容易形成一个线性叙事：

> LLM → Agent → World Model → Robot → BCI

我认为这条线过于整齐，甚至会误导创业判断。

Digital Agent 和 Physical AI 的共同点不是“一个是虚拟执行器，一个是现实执行器”这么简单，而是它们都在形成一个闭环：

> **Observe → Understand → Predict → Plan → Act → Observe Again**

在数字世界，这个闭环面对文件、数据库、浏览器、软件和 API。

在物理世界，它面对空间、物体、摩擦、力、遮挡、能量和人的安全边界。

所以更准确的说法是：

> Agent 是 Digital Agency；机器人是 Physical Agency。

两者是 AI 自主性的两个并行分支。

但不能因此把机器人身体理解成一个简单可替换的“执行器”。

Google DeepMind 2026 年发布的 Gemini Robotics ER 2 很能说明这个问题：高层 embodied reasoning model 负责理解物理世界、多步规划、协同和任务状态跟踪，然后把具体运动执行交给低层 VLA。高层 Reasoning 可以越来越通用，低层 Motor Control 仍然和具体 embodiment 强相关。[Google DeepMind, Gemini Robotics ER 2](https://deepmind.google/models/gemini-robotics/embodied-reasoning/)

换句话说：

> **大脑可能越来越通用，小脑和身体不会那么快通用。**

传感器、自由度、执行器、结构、时延、动力学和安全限制都会反过来决定智能如何落地。

软硬结合不是“给 AI 加个壳”，而是 Model × Data × Control × Sensor × Actuator × Mechanical Design 的共同优化。

## 十二、为什么顶尖 AI 人才去做 World Model，不等于所有创业者都该去做机器人

现在很多一线研究者转向 Spatial Intelligence、World Model 和 Physical AI，这当然是一个重要信号，但也存在明显的选择偏差。

其中至少有三个不同原因。

第一，纯 Language Intelligence 的 Frontier 已经极度拥挤。能够继续做前沿研究的人，自然会寻找尚未被规模化解决的问题：3D、Dynamics、Physics、Manipulation、Long-horizon Planning。

第二，物理世界的 TAM 确实更大。Digital Agent 主要在吞 Cognitive Labor，Physical AI 有机会进入 Physical Labor。制造、物流、农业、建筑、服务业里大量成本并不在软件预算里，而在人、设备和现实运营中。

第三，也是最容易被忽略的：Physical AI 的商业化难度同样高很多。

代码世界可以 Git Reset，物理世界没有 Ctrl+Z。

数字 Agent 的失败可以重试、回滚、沙箱隔离；机器人一次错误可能导致碰撞、损坏、停线甚至人身风险。真实数据采集昂贵，环境长尾更多，每增加一个执行单元还要制造、部署、维护和售后。

所以长期 TAM 更大，不等于近期创业回报更好。

这两个判断可以同时成立：

> **Physical AI 可能是 AI 最大的长期 Frontier；Digital Agent / AI Native Service 仍然是未来 3–5 年更确定的商业化路径。**

## 十三、世界模型的价值，也不应该被简化成“机器人终于有大脑了”

World Labs 在 2026 年把 World Model 分成 Renderer、Simulator、Planner。它真正强调的关键环节，是让 Agent 能在世界里行动、学习和被评估，而不是只生成一个“看起来像真的”视频。

7 月发布的 Real-to-Sim-to-Real 系统，就是把真实环境转成模拟环境，再用于机器人策略训练与评估。[World Labs, Building Worlds That Train Robots](https://www.worldlabs.ai/blog/real-to-sim-to-real)

9 月 1 日，World Labs 又发布 Atlas，把文本、图像、视频和 3D 放进统一 spatial context，并明确把 robotics simulation 作为用途之一。[World Labs, Atlas](https://www.worldlabs.ai/blog/atlas)

这里最值得关注的不是“生成世界”本身，而是 Simulation 开始有机会成为 Physical AI 的训练环境和 Eval 环境。

Coding 为什么容易跑起来？因为代码天然有 Compile、Test、Sandbox。

机器人一直缺的，恰恰是一套同等便宜、可重复、可规模化的训练与验证环境。

如果 World Model 真正带来价值，很可能不是因为它比视频模型更会生成，而是因为它降低了 Physical Agent 获取训练数据、测试策略和发现 Failure Region 的成本。

这又回到同一条产业逻辑：

> **真正值钱的不是能力展示，而是能否进入生产闭环。**

## 十四、BCI 应该单独看，它更像 Biological I/O，而不是另一种机器人

脑机接口也经常和 Physical AI 被放在同一个“AI 进入现实世界”的故事里，但产业逻辑并不一样。

今天的大部分 BCI 主要在解决 Human → Machine 的输入：运动意图、Cursor Control、Speech Decoding；一部分闭环神经调控则包含 Machine → Human 的刺激。

它更接近一个 **Biological I/O Layer**，而不是一个新的 Physical Actuator。

2026 年 Nature Reviews Bioengineering 仍在讨论从 speech BCI 向 language BCI 的演进；同时，植入式 BCI 的长期稳定性、患者间泛化、临床可扩展性和神经数据保护仍然是核心问题。[Nature Reviews Bioengineering, 2026](https://www.nature.com/articles/s44222-026-00460-4)

所以机器人、World Model、BCI 可以共享“AI 正在走出纯文本世界”这条大叙事，但不能用同一套时间表和商业模型判断。

## 十五、把这些方向放在一起，AI 正在进入三个世界

我目前更愿意把未来的 AI 应用分成三条并行路线。

| 世界 | AI 的形态 | 主要行动对象 | 主要价值池 | 当前瓶颈 | 近期商业确定性 |
| --- | --- | --- | --- | --- | --- |
| Digital World | Agent / Operator | 软件、文件、账户、业务流程 | Cognitive Labor / Service / Transaction | Context、权限、可靠性、组织采用 | 最高 |
| Physical World | Robot / Autonomous Machine | 空间、物体、设备、现实任务 | Physical Labor / Asset Utilization | 数据、控制、硬件、可靠性、成本 | 中等 |
| Biological World | BCI / Human Augmentation | 神经系统与人的能力边界 | Healthcare / Augmentation | 临床、稳定性、监管、伦理 | 较低 |

三条路线最终都在做同一件事情：

> 把机器从“给建议”变成“对一个环境持续采取行动”。

但环境不同，产品规律完全不同。

## 十六、AI 应用的价值池，会沿着责任梯度不断扩大

如果从经济价值看，还可以看到另一条很重要的迁移。

最早的 AI 产品主要争夺：

> Software Budget

Agent 开始进入：

> Labor Budget

AI Native Service 进一步进入：

> Outsourcing / Professional Service Budget

真正完成业务结果以后，会继续进入：

> Transaction Budget

Physical AI 再往外扩张：

> Physical Labor + Asset / Operations Budget

可以把它写成：

```text
Capability
    ↓
Software
    ↓
Labor
    ↓
Service
    ↓
Outcome
    ↓
Transaction
    ↓
Autonomous Operation
```

越往下，TAM 越大。

但同时，责任也越重：需要更强的可靠性、Eval、权限、保险、合规、资本和运营能力。

这就是为什么“做一个 AI 功能”越来越容易，而“做一家真正大的 AI 公司”反而不会越来越容易。

## 十七、未来最重要的公司，可能根本不像“AI 应用公司”

如果上面的判断成立，未来最大的 AI 公司不一定长成今天熟悉的 Chatbot 或 Agent App。

它可能看起来就是：

- 一家律所；
- 一家会计服务公司；
- 一家保险理赔公司；
- 一家客服运营商；
- 一家招聘服务公司；
- 一家物流运营商；
- 一家工厂自动化服务商。

只是它的生产函数完全不同。

传统公司：

> Software + 1000 Human Workers → Service

AI Native Company：

> Models + Agents + Workflow + Eval + 100 Exception Handlers → Service

Physical AI 公司则可能进一步变成：

> Models + Robots + Remote Ops + Maintenance → Physical Outcome

因此未来“AI 应用”和“AI 公司”之间的边界会越来越模糊。

公司本身就是应用。

## 十八、下一批机会，我会优先看六种形态

如果基于这套框架扫描未来，而不是追逐某个季度的 VC 风向，我会优先看六类公司。

### 1. Digital Outcome Company

从一个数字化任务切进去，最终对完整业务结果负责。

例如理赔、应收账款、合规、客服、税务、采购、招聘运营。

### 2. AI Native Service

过去主要靠专业人力交付，现在可以通过 AI 把人变成 Exception Layer。

关键不是有没有 Agent，而是 Human Exception Rate 能否持续下降。

### 3. Vertical Transaction Network

不只完成工作，还能进入订单、资金、撮合和资源配置。

这是从 Workflow 进入真正产业利润池的一步。

### 4. Physical Operator

不卖机器人本身，而卖每个搬运、每平方米清洁、每次巡检、每个合格零件。

Physical Result-as-a-Service 可能比单纯硬件销售更接近 AI 的价值捕获方式。

### 5. Human Augmentation Device

智能硬件如果只是“把 ChatGPT 装进另一个壳”，长期价值有限。

真正有意义的是它给 AI 增加什么新的 Observe / Act Channel：第一视角视觉、Always-on Audio、生理信号、空间定位、移动、抓取、身份确认。

### 6. Workload-born Infrastructure

先在真实应用里解决 Eval、支付、权限、Memory、Security 等问题，等 workload 足够大以后再平台化。

这比脱离业务直接赌一个未来标准更稳。

## 十九、相反，我会对五类项目保持高度警惕

第一，**能力 Wrapper**：主要价值来自基础模型暂时不会做。

第二，**通用 Agent 的小号复制品**：没有独特 Context、Distribution 或业务责任。

第三，**提前两层的 Infra**：方向长期正确，但真实 workload 还不存在。

第四，**没有新 Observe / Act 能力的 AI 硬件**：只是换了一个设备壳。

第五，**用长期 Frontier 代替近期产品成立**：世界模型、通用机器人、BCI 都很重要，但“重要”与“适合现在创业”不是一回事。

## 二十、最后，我会用十个问题判断一个 AI 创业机会

以后再看一个 AI 项目，我更愿意先问下面这些问题，而不是先看 Demo。

| 问题 | 好答案 |
| --- | --- |
| 客户真正为什么付钱？ | 为完成工作或结果，而非 AI 功能 |
| 钱现在从哪里支出？ | Labor / Service / Transaction，而不只是 Software |
| 模型能力提升十倍之后呢？ | 自动化率上升，而不是产品消失 |
| 工作是否数字化？ | 输入、状态、动作大部分机器可访问 |
| 结果是否可验证？ | 有清晰完成条件与 Eval |
| Agent 是否能直接行动？ | 不只建议，还能改变业务状态 |
| 每次执行是否产生反馈？ | 能形成 Failure / Correction / Reward 数据 |
| 人工介入是否会持续下降？ | Human Exception Rate 有清晰下降路径 |
| 能否从 Point 扩到 Workflow？ | Wedge 后面有更长责任链 |
| 最终能否进入 Outcome / Transaction？ | 能拿到更大的价值池 |

如果是硬件，再加两个问题：

> 它给 AI 增加了什么以前没有的感知通道？

> 它给 AI 增加了什么以前没有的行动空间？

回答不了，通常就不是 AI Native Hardware。

## 结语：未来真正稀缺的，不是智能，而是“可靠地替人负责”

过去三年，大家一直在讨论 Intelligence 会不会成为 Commodity。

我现在觉得，这个问题已经不是最重要的了。

模型能力继续上升几乎是确定的。更多推理、生成、规划和 Tool Use 会被 Foundation Model 与 General Agent 吸收，也会有大量今天看起来独立的 AI 产品因此消失。

但这不代表应用层没有价值。

恰恰相反，**智能越便宜，真正稀缺的东西越会从“拥有智能”迁移到“让智能进入真实世界并承担责任”。**

在数字世界，这意味着 Context、Permission、Workflow、Eval、Operations 和 Outcome。

在物理世界，这意味着 Sensor、Embodiment、Control、World Model、Safety 和 Reliability。

在生物世界，这意味着长期稳定的 Neural I/O、临床效果和责任边界。

所以 AI 应用的下一站，不是做更多 Agent。

而是让 AI 从一个会说、会想、会调用工具的模型，逐渐变成真正的生产者：

> **完成工作，交付结果，进入交易，并最终在数字世界和物理世界中持续自主运行。**

如果一定要用一句话概括我现在对 AI 应用未来的判断：

> **AI 的产业价值，正在从“能力溢价”迁移到“责任溢价”。模型负责让机器越来越聪明，真正的大公司负责让机器越来越能被托付。**

---

### 参考资料

1. [Menlo Ventures — 2025: The State of Generative AI in the Enterprise](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)
2. [Bessemer Venture Partners — Owning the Outcome: AI-Native Services Evaluation Framework](https://www.bvp.com/atlas/owning-the-outcome-bessemers-ai-native-services-evaluation-framework)
3. [Intercom — Fin AI Agent Outcomes](https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes)
4. [Salesforce — Help Agent Resolutions Usage Types](https://help.salesforce.com/s/articleView?id=ai.usage_flex_credits.htm&language=en_US&type=5)
5. [Abridge — Patient-Centered Clinician Intelligence Platform](https://www.abridge.com/press-release/patient-centered-clinician-intelligence-platform-keynote)
6. [Google DeepMind — Gemini Robotics ER 2](https://deepmind.google/models/gemini-robotics/embodied-reasoning/)
7. [World Labs — Building Worlds That Train Robots](https://www.worldlabs.ai/blog/real-to-sim-to-real)
8. [World Labs — Atlas: A World Model for Spatial Intelligence](https://www.worldlabs.ai/blog/atlas)
9. [Nature Reviews Bioengineering — Transitioning from Speech to Language Brain–Computer Interfaces](https://www.nature.com/articles/s44222-026-00460-4)
