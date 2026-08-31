---
layout: post
title: "RAG 之后，Agent 需要 Context Recommendation"
subtitle: "Harness 把模型周围的运行环境拆成了正式部件，下一步要解决的是每一轮该把哪些信息、能力与权限交给模型。"
date: 2026-08-14 09:14:00 +0800
reading_time: 11
tags:
  - AI Agent
  - Context Engineering
  - DeepSeek Harness
description: Context Recommendation 是 Agent Runtime 的工作台装配层：为每一步选择信息、工具、Skill、状态与权限，同时记录为什么选、为什么不选。
---

DeepSeek Harness 的架构文档里有一句话：

> `agent/pre-step decides what the model sees.`

`agent/pre-step` 决定模型看到什么。

我认为这句话比 “Everything is a Plugin” 更值得讨论。

过去做 Agent，大家习惯问三个问题：模型够不够强，工具接得够不够多，上下文窗口够不够大。Harness 把问题往前移了一步：即使模型、工具和资料都已经在那里，下一轮究竟该把什么交给模型？

假设一个 Agent 正在写产品立项。

第一步，它需要行业资料和用户研究；第二步，它要读回已经确认的产品边界；第三步，它需要表格与计算工具；准备修改正式文件时，它还要知道自己有没有写权限、哪些动作必须由人确认。

这四步可以用同一个模型，却不能使用同一份工作台。

以前我把 RAG 之后的这个问题叫作 **Context Recommendation**。当时想的主要是资料检索与排序。看完 DeepSeek Harness 的公开架构后，我会把定义扩大：

> Context Recommendation 是 Agent Runtime 的工作台装配层。它为下一步选择模型该看到的信息、可调用的能力和必须遵守的权限，也决定哪些内容暂时不该出现。

DeepSeek Harness 没有在公开文档中声称已经完成了一套 Context Recommender。它做的事情更基础：把“每一步给模型什么”从 Prompt 里的隐性操作，变成运行时可以组装、注入、限制和回放的正式接口。

## RAG 找资料，Agent 还要组工作台

2020 年的 RAG 论文解决了一个很具体的问题：当模型参数里的知识不足时，先从外部知识库找到与问题相关的段落，再让模型基于这些材料生成答案。[RAG 原始论文](https://arxiv.org/abs/2005.11401)

工程实现后来不断扩展，主问题仍然可以概括成一句话：

**哪些资料和当前问题有关？**

Agent 面对的范围更大。

一段历史对话是 Context，一份研究报告是 Context，当前文件状态是 Context；这一步能不能调用浏览器、代码环境或某个 Skill，也是 Context；另一个 Agent 刚发现的异常、用户刚撤回的要求、一次删除操作必须得到确认，同样会改变下一步。

RAG 通常交付“可供回答的材料”。Agent Runtime 要交付的是一张可以继续工作的桌子：资料放哪些，工具开哪些，当前状态是什么，边界画在哪里。

这也是为什么上下文窗口变长，问题没有自动消失。

容量回答“能不能装下”，不回答“现在该不该出现”。

《Lost in the Middle》在多文档问答和键值检索实验中发现，同一条关键信息只因处在长上下文中的位置不同，模型表现就可能明显变化；位于开头或结尾的信息往往更容易被利用。[Lost in the Middle](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long)

这项研究不能简单推出“长上下文没用”，不同模型的表现也会继续变化。它至少说明，装得下和用得好不是同一个问题。

开定价会时，产品经理不会把五年邮件、整个代码库和所有客服日志一起摊在桌上。他会带成本、竞品和支付意愿，也会标出哪些数字过期、哪些结论仍有争议。

Agent 也需要这种随步骤变化的工作台。

## Harness 把选择发生的位置露了出来

DeepSeek Harness 把模型周围的多个部分做成插件：模型适配器、工具注册表、session log，甚至 agent loop。官方仓库目前仍把项目标为可能发生兼容性变化的 developer preview。[DeepSeek Harness 官方仓库](https://github.com/deepseek-ai/deepseek-harness)

其中几处设计与 Context 直接相关。

- `core/system-prompt` 组装这一轮的 prompt section 与工具 schema；
- scoped tool registry 让不同 Agent 获得不同的工具集合；
- `agent/pre-step` 可以在模型请求前接收、改写或拒绝本轮消息；
- `agent.inject()` 把新 Context 放进下一次被接纳的请求；
- append-only session log 保存过程事实，再从日志派生模型历史。

官方[架构文档](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md)还明确规定，送进模型的内容应该能够从日志重建。模型当时看到了什么，不该只存在于一次不可追溯的 Prompt 拼接中。

这套机制可以画成一条很短的链：

> Session / Memory / Knowledge / Tools  
> ↓  
> `agent/pre-step`：选择、过滤、组装  
> ↓  
> Model-visible workbench  
> ↓  
> Action / Tool result / New event  
> ↓  
> 写回 Session，进入下一轮选择

Harness 已经给出了装配工作台的位置，但没有替产品做出选择。哪些内容值得进入，哪些工具应该隐藏，何时注入一条新信息，仍然需要一层策略。

这层策略，就是我所说的 Context Recommendation。

## Context 不只是文档

如果把 Context 继续理解成“参考资料”，Agent 的很多失败会散落在不同模块里。

我会先把它分成六类。

| 类型 | 典型内容 | 选错后的结果 |
| --- | --- | --- |
| Instruction | 角色、目标、规则、输出契约 | 局部动作没错，任务方向偏了 |
| Memory | 用户偏好、历史决定、项目承诺 | 重复追问，或推翻已经确认的边界 |
| Knowledge | 文档、网页、代码、数据库与研究证据 | 使用无关、过期或不可信的信息 |
| Capability | Tool、Skill、API、Sub-agent | 找不到该用的能力，或在过多工具中选错 |
| State | 当前文件、任务阶段、环境变化与中间结果 | 按旧状态继续行动，重复或覆盖工作 |
| Authority | 可读范围、写权限、审批条件与风险等级 | 越权读取，或绕过高风险确认 |

这六类不会全部变成自然语言。

Capability 可能表现为这一轮暴露的工具 schema。Authority 一部分可以告诉模型，另一部分必须由执行层强制检查。State 可能来自结构化事件，Memory 也可能只是指向一条已经确认的决定。

把它们放在同一个系统里，是因为它们共同决定了一件事：模型此刻理解什么、能做什么，出错后由谁负责。

## 为什么要叫 Recommendation

Context Routing、Context Selection、Context Management 都说得通。

我仍然使用 Recommendation，是因为它面对的不是一次固定路由，而是一个不断变化的候选集合。

当前任务可能有两百项候选 Context：正式规则、历史讨论、研究材料、代码文件、工具、Skills、外部事件和其他 Agent 的结果。系统要根据当前步骤生成候选，先过权限与风险门，再排序、压缩和组合，最后形成模型这一轮看到的工作台。

最小流程可以写成：

> Task State → Candidate Generation → Policy Gate → Ranking → Composition → Injection → Outcome → Task State

这里不一定需要一套复杂的机器学习模型。

权限适合确定性规则；固定目标可以常驻；文档候选可以用检索和 rerank；任务走到新阶段时，再由状态机或模型参与判断。Recommendation 描述的是产品职责，不限定具体算法。

如果要让团队先对排序逻辑达成共识，我会写一条粗糙的产品函数：

> 下一步效用 = 任务相关性 × 可信度 × 新鲜度 × 可行动性 × 权限匹配 − Token 成本 − 干扰 − 风险

它不是研究公式，只是一张检查表。

一份旧报告可能高度相关，但新鲜度很低；一个工具很能干，当前 Agent 没有权限时仍然不能出现；一段用户原话可信，却未必支持下一步动作；某条信息只占几十个 Token，也可能因为与正式指令冲突而带来很大干扰。

任务不同，权重也会变。

修代码更依赖仓库状态、错误日志和执行工具。做行业研究更看来源、时间与反证。涉及删除、付款、发信或控制真实设备时，权限与风险要先于相关性。

这件事不能只靠向量相似度解决。

## 推荐什么，和不推荐什么同样重要

Agent 产品很容易把“接入更多”当作能力增长。

接入更多工具、Memory 和数据源当然会扩大上限，也会扩大干扰面。

半年前的临时决定可能被误当成长期规则，旧市场数据会和新事实冲突，五十个相似工具会增加误选，与当前任务无关的个人信息也没有必要进入请求。一个带写权限的工具即使没有被调用，只要对模型可见，也可能改变它的计划。

所以 Context Recommender 必须做负推荐：

- 资料相关但已经过期，只作为历史背景；
- 工具有能力完成任务，但当前 Agent 没有权限；
- Memory 属于另一位用户，不进入当前工作台；
- Sub-agent 给出了结论，却没有证据，不改变主任务状态；
- 中间结果已经被新事件替代，留在日志里，不再进入工作集。

Session log 负责保存“发生过什么”。Context Recommendation 负责决定“这一刻还要让模型看到什么”。

日志应该完整，工作集应该克制。

## 这套系统要怎样被验证

Context Recommendation 的目标不是让模型“感觉信息更充分”，而是提高每一步的完成质量，并减少无关暴露与越权风险。

至少要记录六类结果：

1. 完成下一步必需的 Context，有多少被选中；
2. 进入请求的内容中，有多少没有被使用，甚至造成干扰；
3. Tool 与 Skill 是否在需要时出现、不需要时隐藏；
4. 过期、冲突和低可信信息有没有被清楚标记；
5. 权限过滤与人工确认有没有挡住越权动作；
6. 在不同 Context 组合下，任务完成率、返工、Token、延迟和成本怎样变化。

运行记录还要补上一层：候选是什么，选了什么，排除了什么，理由是什么，模型随后做了什么。

只有任务结果，没有当时的选择依据，很难判断失败来自模型、工具，还是工作台装错了。

可以先从人工金标准开始。挑一组步骤清楚的真实任务，由人标注每一步的必需 Context、可选 Context、禁止 Context 与能力集合，再做消融：去掉某一项后任务是否失败，加入某一项后错误是否增加。

这比把“点击率”当作推荐质量，更接近 Agent 的工作目标。

## RAG 会留在系统里，但位置会改变

Context Recommendation 不取代 RAG。

RAG 仍然可以负责从知识库、代码库或 Memory 中生成候选。变化在它之后：检索结果还要和任务状态、固定指令、工具、Skill 与权限一起经过选择，才进入模型这一轮的工作台。

| | RAG | Context Recommendation |
| --- | --- | --- |
| 主要对象 | 外部知识与文档片段 | 信息、能力、状态与权限 |
| 触发时机 | 问题或检索请求 | Agent 的每一个关键步骤 |
| 主要输出 | 相关材料 | 下一步的模型工作台与执行边界 |
| 主要审计 | 找到了什么、来源在哪里 | 看到了什么、为什么出现、允许做什么 |

DeepSeek Harness 也没有证明 Context Recommendation 已经跑通。

它证明的是，模型周围的运行环境可以被拆成正式部件；本轮输入、工具与状态可以被组装；模型可见内容能够被回放；不同 Agent 可以拥有不同的能力集合。

同一个模型，在不同的工具、Memory 与权限组合下，会表现得像不同的 Agent。所以 RAG 之后的问题，不是还能往窗口里塞多少东西。

`agent/pre-step` 已经决定模型看到什么。

接下来要回答的是：这一刻，它应该看到什么；为什么是这些；我们怎样知道这次选择帮到了任务。

---

## 延伸资料

- [DeepSeek Harness 官方仓库](https://github.com/deepseek-ai/deepseek-harness)
- [DeepSeek Harness Architecture](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md)
- [DeepSeek Harness `dsh-session`](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/core/session/README.md)
- [Lewis et al.：Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [Liu et al.：Lost in the Middle](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long)
