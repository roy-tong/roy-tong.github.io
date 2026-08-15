---
layout: post
lang: en
title: "After RAG, Agents Need Context Recommendation"
subtitle: "DeepSeek Harness turns the runtime around the model into formal parts. The next problem is deciding what information, capabilities and permissions each step should receive."
date: 2026-08-14 09:14:00 +0800
reading_time: 11
tags:
  - AI agent
  - context engineering
  - DeepSeek Harness
description: Context Recommendation is the workbench assembly layer of an Agent Runtime — selecting the information, tools, skills, state and permissions for each step, and recording why each choice was made.
permalink: /en/notes/agent-context-recommendation-after-rag/
---

The DeepSeek Harness architecture documentation contains one line:

> `agent/pre-step decides what the model sees.`

I think that line deserves more discussion than "Everything is a Plugin."

When people build agents, they habitually ask three questions: is the model strong enough, are enough tools connected, is the context window big enough. Harness moves the question one step earlier: even when the model, tools and materials are all in place, what exactly should be handed to the model in the next step?

Consider an agent writing a product kickoff document. First it needs industry research and user studies; second, it must read back the confirmed product boundaries; third, it needs spreadsheet tools; and before editing the formal file, it must know whether it has write permission and which actions require human confirmation. Four steps, the same model — but not the same workbench.

I used to call the post-RAG version of this problem **Context Recommendation**, when I was mainly thinking about retrieving and ranking material. After reading Harness's public architecture, I'd expand the definition:

> Context Recommendation is the workbench assembly layer of an Agent Runtime. For the next step it selects the information the model should see, the capabilities it may call, and the permissions it must obey — and what should not appear at all.

DeepSeek Harness does not claim to have completed a Context Recommender. What it does is more fundamental: turning "what we give the model at each step" from an implicit operation inside prompts into an official interface the runtime can assemble, inject, restrict and replay.

## RAG finds material; agents assemble a workbench

The 2020 RAG paper solved a concrete problem: when knowledge in a model's parameters is insufficient, first retrieve relevant passages from an external knowledge base, then generate answers grounded in that material. [Lewis et al.: Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) Engineering expanded endlessly afterward, but the main question still reduces to one sentence: **which materials are relevant to the current question?**

Agents face a much larger scope. A conversation history is context; a research report is context; the current file state is context; whether this step may call a browser, a code environment or a Skill is context; an anomaly found by another agent, a requirement the user just withdrew, a deletion that must be confirmed — all of it changes the next step.

RAG usually delivers "material to answer with." An Agent Runtime must deliver a table you can keep working on: which materials are placed, which tools are open, what the current state is, where the boundaries are drawn. This is why a longer context window doesn't make the problem disappear: capacity answers "can it fit?", not "should it be present right now?"

"Lost in the Middle" found that the same critical information produces measurably different model performance depending on its position in a long context; information at the beginning or end is used more readily. [Liu et al.: Lost in the Middle](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long) That doesn't imply long context is useless, but it does show that fitting and using are different questions.

When a product manager runs a pricing meeting, he doesn't spread five years of email, the whole codebase and all support logs across the table; he brings costs, competitors and willingness-to-pay, and flags stale numbers and contested conclusions. Agents need this kind of step-varying workbench too.

## Harness exposes where the choice happens

DeepSeek Harness makes the parts around the model pluggable: model adapters, a tool registry, session logs, even the agent loop. The official repository still labels the project a developer preview subject to compatibility changes. [DeepSeek Harness repository](https://github.com/deepseek-ai/deepseek-harness) Several design choices relate directly to context:

- `core/system-prompt` assembles this turn's prompt sections and tool schema;
- the scoped tool registry gives different agents different tool sets;
- `agent/pre-step` can receive, rewrite or reject the next message before the model request;
- `agent.inject()` puts new context into the next accepted request;
- the append-only session log stores process facts, and model history is derived from the log.

The official [architecture documentation](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md) also requires that whatever is sent to the model can be reconstructed from the log — what the model saw should not exist only in an untraceable prompt concatenation.

The mechanism forms a short chain:

> Session / Memory / Knowledge / Tools
> ↓
> `agent/pre-step`: select, filter, assemble
> ↓
> Model-visible workbench
> ↓
> Action / Tool result / New event
> ↓
> Written back to Session → next round of selection

Harness provides the place where the workbench is assembled, but it does not make the product's choices. Which content deserves to enter, which tools should be hidden, when to inject new information — that still needs a policy layer. That layer is what I call Context Recommendation.

## Context is not just documents

If you keep reading "context" as "reference material," agent failures get scattered across modules. Start by splitting it into six types.

| Type | Typical content | What goes wrong if mis-selected |
| --- | --- | --- |
| Instruction | Role, goals, rules, output contracts | Local actions are fine; the whole task drifts |
| Memory | User preferences, past decisions, project commitments | Repeated questioning, or overturning confirmed boundaries |
| Knowledge | Documents, web pages, code, databases, research evidence | Using irrelevant, stale or untrustworthy information |
| Capability | Tools, Skills, APIs, sub-agents | The needed capability is missing, or the wrong one is picked from too many |
| State | Current files, task stage, environment changes, intermediate results | Acting on old state; duplicating or overwriting work |
| Authority | Read scope, write permissions, approval conditions, risk levels | Reading beyond authority, or bypassing high-risk confirmation |

Not all six become natural language. Capability may show up as the tool schemas exposed this turn; part of Authority can be told to the model, the rest must be enforced by the execution layer; State may come from structured events; Memory may be a pointer to an already-confirmed decision. They belong in one system because together they decide one thing: what the model understands right now, what it can do, and who is accountable when it goes wrong.

## Why call it Recommendation

Context Routing, Context Selection, Context Management — all defensible names. I keep "Recommendation" because this is not a fixed route; it is a changing candidate set. The current task may have two hundred candidate contexts: official rules, past discussions, research material, code files, tools, Skills, external events, other agents' results. The system generates candidates, passes them through permission and risk gates, then ranks, compresses and composes them into the workbench for this turn.

The minimal pipeline:

> Task State → Candidate Generation → Policy Gate → Ranking → Composition → Injection → Outcome → Task State

This doesn't require a sophisticated ML model: permissions fit deterministic rules; fixed goals can stay resident; document candidates can use retrieval plus reranking. Recommendation describes a product responsibility, not a specific algorithm.

If I want a team to agree on the ranking logic first, I'd write a rough product function:

> next-step utility = task relevance × trustworthiness × freshness × actionability × permission match − token cost − distraction − risk

It is not a research formula; it is a checklist. An old report can be highly relevant and low on freshness; a capable tool must not appear when the agent lacks permission; a verbatim quote can be trustworthy and still not support the next action; a few dozen tokens can still cause large distraction by conflicting with standing instructions. Weights change with the task: code repair leans on repository state, error logs and execution tools; industry research cares about source, recency and counter-evidence; for deletion, payment, messaging or real-device control, permission and risk outrank relevance. Vector similarity alone cannot solve this.

## What you don't recommend matters as much as what you do

Agent products easily mistake "connect more" for capability growth. More tools, memory and data sources raise the ceiling — and widen the surface of distraction. A half-year-old ad hoc decision can be mistaken for a standing rule; fifty similar tools increase mis-selection; a write-capable tool that is never called can still change the model's plan merely by being visible.

So a Context Recommender must do negative recommendation:

- Relevant but stale material appears only as historical background;
- A tool that could do the job stays hidden when the agent lacks permission;
- Memory belonging to another user never enters the workbench;
- A sub-agent's conclusion without evidence doesn't change the main task's state;
- Intermediate results superseded by newer events remain in the log, out of the working set.

The session log records "what happened." Context Recommendation decides "what the model should still see this moment." Logs should be complete; the working set should be restrained.

## How to validate such a system

Context Recommendation is not about making the model "feel better informed." It is about raising per-step completion quality and reducing irrelevant exposure and over-authorization risk. Record at least six kinds of outcomes:

1. How much of the context needed for the next step was selected;
2. How much of what entered the request went unused, or actively distracted;
3. Whether Tools and Skills appear when needed and hide when not;
4. Whether stale, conflicting and low-trust information is clearly marked;
5. Whether permission filtering and human confirmation blocked out-of-bounds actions;
6. How task completion, rework, tokens, latency and cost change across context combinations.

The run log needs one more layer: what the candidates were, what was selected, what was excluded, why, and what the model did next. With only task outcomes and no record of the selection rationale, you can't tell whether a failure came from the model, the tools, or a wrongly assembled workbench. Start with a human gold standard: label the required, optional and forbidden context for each step of real tasks, then ablate — remove one item and see whether the task fails, add one and see whether errors increase. That is closer to an agent's actual objective than treating click-through rate as recommendation quality.

## RAG stays in the system — in a different position

Context Recommendation does not replace RAG. RAG can still generate candidates from knowledge bases, codebases or memory; the change comes after it: retrieval results must pass through selection together with task state, standing instructions, tools, Skills and permissions.

| | RAG | Context Recommendation |
| --- | --- | --- |
| Primary object | External knowledge and document passages | Information, capabilities, state and permissions |
| Trigger | A question or retrieval request | Every critical agent step |
| Main output | Relevant material | The next step's model workbench and execution boundaries |
| Main audit | What was found, where it came from | What was seen, why it appeared, what was allowed |

RAG becomes one candidate generator inside this system — not a legacy approach to be retired.

DeepSeek Harness doesn't prove Context Recommendation works, either. What it proves: the runtime around a model can be decomposed into formal parts; per-turn inputs, tools and state can be assembled; model-visible content can be replayed; different agents can hold different capability sets.

The same model with different tools forms different plans; with different memory it carries different history; under different permission constraints it stops at different boundaries; seeing different context at each step, it eventually behaves like a different agent.

So the post-RAG question is not how much more we can stuff into the window. `agent/pre-step` already decides what the model sees. The next question is: what should it see at this moment, why these things, and how do we know this selection helped the task.

---

## References

- [DeepSeek Harness repository](https://github.com/deepseek-ai/deepseek-harness)
- [DeepSeek Harness Architecture](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md)
- [DeepSeek Harness `dsh-session`](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/core/session/README.md)
- [Lewis et al.: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [Liu et al.: Lost in the Middle](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long)
