---
layout: post
lang: en
title: "One Person, One AI Agent, Three Products: I Wrote the Company into Code"
subtitle: "How one person runs three products: the agent advises, the kernels execute, I hold the gate. Discipline lives in code, not in good intentions."
date: 2026-10-31 08:30:00 +0800
reading_time: 5
tags:
  - agents
  - product method
  - working model
description: "The question I get most is arithmetic, not technical — how does one person run three products? The answer is not overtime. It is three roles on one loop: the agent advises, the product kernels execute, and I am the gate."
---

The question I get most often is not technical. It is arithmetic: "You're one person. How do you run three products?"

I used to explain seriously: the three products share one reasoning chain and one evidence contract, so the marginal cost is low… and halfway through, faces would go politely blank. So I changed the answer. One sentence:

**I am not one person doing three products. I am three roles running one loop — and two of those roles are not human.**

## Three products, one loop

First, the products. Each owns one segment of the loop:

**[Askovo](https://github.com/roy-tong/askovo) does research** — the "what should we build" question. Feed it a product idea; it returns judgments with evidence grades, reasoning from scenes, users, pains, and needs through to features, product, and business — seven nodes, each edge carrying its rationale. Every claim gets an evidence grade (E0–E5); when a conclusion outruns its data, the audit command says so outright, with exit code 1 you can put in CI. Open source.

**[Verovo](https://github.com/roy-tong/verovo) does verification** — the "did it actually get done" question, from the buyer's side of AI services: can you trust the vendor's bill, did delivery meet the bar. Criteria checks run locally, bills can be recounted, and acceptance and renewal decisions have evidence behind them. It evolved out of my earlier AgentMeasure.

**[Growovo](https://github.com/roy-tong/Growovo) does growth** — the "will anyone pay" question. Feed it a shipped product; it delivers verifiable real-user growth — signups, activation, payment — with evidence at every step.

Research tells you what to build. Verification tells you whether it got built. Growth tells you whether anyone pays. It is one upstream–downstream line: before development, Askovo takes research end-to-end — from study design and collection through audit and delivery; after launch, Growovo takes growth end-to-end — from positioning and asset building through channel execution and attribution. **Each engine closes its own loop.** This is not "one product does all the reasoning, another does all the executing" — reasoning and execution come paired inside every product: Askovo's collection and audits are execution; Growovo's positioning and channel strategy are reasoning. What crosses the boundary between them is one thing only: graded evidence. Askovo's judgments feed Growovo's positioning; Growovo's first-hand feedback flows back into research, carrying its evidence grade.

## Three roles, each holding one line

But the real point is not the products. It is the division of labor. Three roles:

**The AI agent advises.** It lives inside my code repositories: reading code, drafting plans, building the website, editing copy, fixing CI, running research. Judgment and output are its strengths — the first draft of this very essay was written by it.

**The product kernel executes.** Outbound actions are where I stop trusting the agent's instincts — in Growovo, which owns outbound motion, the kernel is the executor: publish, reply, message, engage — all actions go through one pipeline. Gate checks first, then throttling; after sending, read-back verification, screenshots, and a ledger entry. Every write is dry-run by default; nothing goes out without an explicit `--go`.

**I am the gate.** No plan runs without my review. No exceptions.

These three roles are the operating discipline **inside** each product, not a division between products — Askovo's collection and audits and Growovo's positioning and campaigns all run under the same rule.

These three sentences are not management theory I invented. They sit on the first screen of Growovo's README: the agent advises, the kernel executes, the human holds the gate.

## Discipline belongs in code, not in good intentions

Why so strict? Because an agent's discipline is **a property of the conversation** — change the model, the session, the prompt, and the discipline changes with it. A kernel's discipline is **a property of the code**: dry-run by default, throttle tables, read-back checks — written into the program, identical no matter who operates it.

So my standard is simple: **the ceiling must be a property of the kernel, not of anyone's self-discipline.**

That is also why I turn capabilities into products instead of leaving them inside agent sessions. Four reasons:

1. **Reusable** — the capability survives the conversation;
2. **Auditable** — every action has a ledger, an evidence grade, a screenshot;
3. **Provable limits** — the safety boundary lives in code, not in promises;
4. **Unbound** — any agent, any person, operates the same kernel.

Put the other way: a capability that exists only in a conversation between me and an agent is not an asset. It is a chat log.

## One table

In daily work, the decision rule fits in one table:

| Situation | Who does it |
|---|---|
| Producing *things*: websites, copy, code, research plans | The agent, directly |
| Outbound *actions*: posting, replying, messaging | Agent drafts → kernel executes → I approve |
| Anything that repeats, needs a ledger, or needs throttling | Must be productized. Never left in a session. |

## Evidence is the common currency

The last piece: all three products share one evidence-grading scheme. Askovo's research claims carry E0–E5; Growovo's growth actions reuse the same grades.

So "research says the demand exists" and "growth says users arrived" speak the same language. If research says the evidence is insufficient, growth cannot fill the gap with imagination — and the first-hand feedback growth collects flows back into research, carrying its own evidence grade. The three kernels cannot talk past each other.

## An honest status report

This model has not been running for long. Askovo is open source and usable today; Verovo and Growovo are early — repositories public, capabilities arriving on a schedule. I do not call a design "validated" — that red line is shared by all three: every claim must be able to point at its evidence, and when the evidence runs short, say so.

So here is the full answer to "how does one person run three products": I am not working myself to death. I am translating a company's job descriptions into code. Research, verification, growth — one kernel each. The agent is the advisor. I am the only gate.

The company got written into code, and the human does only what code cannot: judge, and be accountable.
