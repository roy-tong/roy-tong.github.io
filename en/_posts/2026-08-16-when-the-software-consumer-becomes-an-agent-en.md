---
layout: post
lang: en
title: "When the Software Consumer Becomes an Agent"
subtitle: "Seats, installs, and pageviews are breaking. Measurement is the missing infrastructure of the AI economy."
date: 2026-08-16 14:00:00 +0800
permalink: /en/notes/when-the-software-consumer-becomes-an-agent/
reading_time: 10
tags:
  - agents
  - capability economy
  - measurement
  - caas
description: "Software consumers are changing from humans to agents, and the old measurement chain — installs, seats, pageviews — breaks at every link. Measurement precedes payment: the flagship essay for AgentMeasure on why verifiable measurement is the missing infrastructure of the AI economy."
---

The software consumer is changing from humans to agents. It is already happening — most people just haven't yet treated it as something that deserves serious attention.

Two numbers illustrate the speed. On Vercel's skills.sh leaderboard, the top skill accumulated roughly 2 million installs in five months; the MCP ecosystem's SDK downloads were approaching the 100-million-per-month scale by mid-2026. The numbers themselves don't matter. What matters is what they mean: **agents are becoming a new class of software consumer, and the entire measurement system the software industry built for human consumers fails almost completely for them.**

This essay makes three points: why the old metrics break, why measurement must precede payment, and why an open, verifiable measurement layer is the infrastructure everyone is skipping — and no one can eventually avoid.

## 1. The old measurement chain breaks at every link

The human software economy runs on a measurement language decades old: downloads, installs, MAU, seats, pageviews, session time. It rests on an implicit chain:

```text
Installed → Available → Presented → Chosen → Used → Value created
```

For decades this chain worked because each link corresponded to an observable human behavior. Now the consumer on the chain is an agent — and agent behavior breaks the chain at every single link:

- **Installed ≠ available.** An MCP server in a config file is not a capability that was ever invoked in a task.
- **Available ≠ presented.** Agents only surface a capability into the candidate set when the model deems it relevant — a filtering process that is largely invisible from outside.
- **Presented ≠ chosen.** Choice happens inside the context window. It is the result of reasoning, not an auditable click.
- **Chosen ≠ used.** The call may fail, time out, hit a guardrail, or be cancelled by the user.
- **Used ≠ value created.** A successful call can accomplish nothing; a failed call can consume the most expensive resources.

Worse, almost every "usage" signal in the ecosystem today is **self-reported**. skills.sh install counts come from CLI client telemetry — gameable, with no public stats API. The official MCP registry explicitly does not provide adoption or usage data. A third-party audit of the llms.txt ecosystem found that of ~39,000 declared files, 97% had never received a single AI request — *declared ≠ used*. These are not defects of individual platforms; they are a structural gap: **there is no verifiable, standardized measure of "agent usage" anywhere in the ecosystem.**

## 2. Measurement precedes payment

In 2026 the payment layer is arriving fast: Cloudflare's x402 / Agentic Payments, Coinbase's Bazaar, OpenAI and Stripe's Agentic Commerce Protocol (ACP). These protocols solve the same problem: how agents pay for software capabilities.

But they all quietly assume one thing: **that the usage being billed is trustworthy.** That is a dangerous default. You cannot bill for a usage behavior you cannot measure and verify — no meter, no electricity bill. Measurement is the precondition for metering, and metering is the precondition for payment. The layers must be built in order:

```text
Measure → Meter → Pay
```

Everyone's attention is on the rightmost layer. The leftmost layer — verifiable measurement — is the weakest and most absent of all. x402 can transport a credential that says "used 3 times"; it cannot tell whether "used 3 times" is true. This is not a flaw of payment protocols. It is the foundation under them that has not yet been poured.

## 3. What to measure: the five-link chain

The common language AgentMeasure proposes is a five-link chain:

```text
Reach → Choice → Use → Utility → Value
```

- **Reach:** how widely did the agent see this capability? Indexed, retrieved, present in the candidate set?
- **Choice:** among candidates, what was chosen and why? What context and constraints shaped the choice?
- **Use:** did the call happen, and did it deliver? What was invoked and consumed?
- **Utility:** what did the call produce? Did it actually contribute to the task?
- **Value:** how much exchangeable value was created? The only link that leads directly to transactions.

Each link needs its own definition and its own observation. Collapsing all five into a single "usage" number is just inventing a new unverifiable black box.

## 4. Evidence discipline: verifiability is the precondition of social proof

Over the past two years, open source has developed a strong appetite for social proof of AI usage — stars, badges, leaderboards, everyone looking for evidence that "my project is being used by AI." But the value of that proof depends entirely on one thing: **verifiability**.

Stars can be bought. Installs can be gamed. Self-reported telemetry can be faked. Verifiable measurement cannot — if it carries the observation context (where the event was observed: agent runtime, gateway, or server-side self-report?) and execution validity (did the attempt actually deliver?), and grades its claims by evidence strength (E0–E5, from pure self-report to auditable independent observation), it stops being a marketing number and becomes a **falsifiable fact**.

That is exactly what the AI economy is scarcest in: falsifiable facts. Markets, rankings, billing, and insurance all sit on that foundation.

## 5. Why it must be an open standard

A measurement language cannot be any vendor's black box. The reason is practical: if the measurement semantics are privately defined by one platform, every market, ranking, and billing system built on them becomes that platform's tenant; if the semantics cannot be publicly audited, the whole system regresses to the self-report era.

So AgentMeasure's route is: an open data language (reach / choice / use / utility / value) plus measurement semantics (observation context, attempt validity, evidence grading) plus machine-readable registry and conformance checks — so markets, metering, and payment protocols can build on a public, auditable fact layer. The standardization window is open right now, in 2026 — AAIF was founded, OpenTelemetry's GenAI semantic conventions are still in development. Whoever defines verifiable "agent usage" in this window owns the next npm download count.

## 6. Where things stand

This layer is not a concept. The AgentMeasure repository already contains:

- **The Core Specification** (Draft 0.4.3): measurement objects, three-layer structure, interaction classes, observability states, metric eligibility, qualification (Context × Validity), measurement labels, and standard invariants;
- **A reference implementation**: an end-to-end pipeline from Provider SDK → Canonical Observation → Collector → Metrics;
- **Measurement Report #001**: local synthetic-traffic verification, including how fail-closed semantics behave in a real pipeline;
- **A benchmark draft**: how to run evidence-graded audits of "usage" claims across the ecosystem;
- **Conformance**: check vectors between the standard and implementations.

The 1.0 graduation criteria are explicit: two independent implementations, three runtime profiles, two tool-side implementations, public conformance and canonical test vectors, 5–10 real projects, a published discrepancy report, and security and privacy review. This is not a "write another spec" project; it is a closed loop from spec to implementation to verification.

## Closing

One line for each of three audiences:

- **To platform teams:** usage stats you ship without verifiability will become the starting point of the next trust crisis. Put the semantics and evidence into your spec now.
- **To open-source maintainers:** stars depreciate; verifiable usage evidence does not. Put "used by agents" evidence in your README instead of another self-reported badge.
- **To founders:** metering is payment's foundation. While everyone is building the payment layer, there are still almost no bricks in the foundation — that is the window.

The software consumer is changing from humans to agents. The last time the software consumer changed, the industry reinvented software economics. This time, it starts with measurement.

---

*Related:* [Whitepaper — How Software Usage by AI Agents Should Be Measured](/en/notes/how-agent-usage-should-be-measured/) · [中文版文章](/notes/when-the-software-consumer-becomes-an-agent/) · [AgentMeasure repository](https://github.com/roy-tong/AgentMeasure) · [Core Specification](https://github.com/roy-tong/AgentMeasure/blob/main/standard/CORE.md) · [Benchmark draft](https://github.com/roy-tong/AgentMeasure/blob/main/benchmark/BENCHMARK-DRAFT.md)
