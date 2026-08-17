---
layout: post
lang: en
title: "Every Agent Usage Number Is Self-Reported"
subtitle: "A field audit of six real claims, and what it means for the agent economy"
date: 2026-08-17 00:30:00 +0800
reading_time: 8
tags:
  - agent
  - measurement
  - benchmark
  - capability economy
description: "We audited six real 'agent usage' claims from live ecosystem discussions and graded them on an evidence ladder. One pattern: every number is self-reported. Independence beats volume; nobody publishes the unit definition. This is the measurement gap the agent economy hasn't admitted yet."
permalink: /en/notes/every-agent-usage-number-is-self-reported/
---

*Field audit conducted 2026-08-16 as part of [AgentMeasure Benchmark Run #001](https://github.com/roy-tong/AgentMeasure/blob/main/reports/benchmark-run-001.md). All claims are real, cited, and replayable.*

## The experiment

"Agent usage" is becoming the social proof of 2026 — the basis for badges, comparisons, metering, and payment. So we went looking for real, public usage claims and asked one question of each: **can this number be verified?**

Six claims, six sources, one afternoon of reading:

| Claim | Where | Grade |
|---|---|---|
| "x402 settled its 162-millionth payment; average ticket $0.25" | X post, 2026-08-13 | E1 |
| "48k active merchants on Base x402 in 30 days" | X post, 2026-08-16 | E1 |
| "~39,000 llms.txt files; 97% received zero AI requests" | third-party audit | E3 |
| "ClaudeBot impersonation up 400% this quarter" | security vendor post | E0/E1 |
| MCP server score badges | registry (glama.ai) | E2/E3 |
| "42 calls, 126 observations, 0 rejections" | our own report (synthetic) | E2 |

The grading ladder (E0–E5): no evidence → self-reported aggregate → disclosed method → third-party verification → independent observation → cross-checked observation.

## What we found

**1. Every number is self-reported.** The difference between the claims was not honesty but *replayability*. Two x402 numbers are probably true and impossible to verify — no disclosed counting method, no public raw data. The impersonation statistic is unverifiable and its key term undefined.

**2. The strongest claim came from the only independent observer.** The llms.txt audit (E3) beat every platform with perfect data. Independence beats volume.

**3. Badges are the weak link.** A registry badge inherits the verification semantics of its source. A badge with no disclosed method is a low grade wearing high-grade colors.

**4. Nobody publishes the unit definition.** None of the six claims states what counts as "a payment", "a merchant", "an AI request", or "an impersonation". This is the gap that matters: you cannot audit what you cannot define.

## Why this matters now

Payment rails are being built on top of these numbers. When x402 settles 162 million payments at $0.25 each, a misdefined unit is a financial-integrity problem, not an analytics problem. The agent economy is about to route real money through measurements nobody can verify.

## The standard's job

This is why AgentMeasure exists: to make E3 cheap, not to moralize about E1. Concretely:

- **Unit definitions must ship with every public metric.** What counts as an attempt, an operation, a delivery, a consumed result — stated, not implied.
- **Observation happens at the callee boundary.** Callers cannot self-report their own usage; that is the difference between a measurement and a press release.
- **Unknown is the default.** Every observation starts unqualified and is upgraded only by evidence. CI, benchmarks, and health checks cannot quietly pollute public numbers.

The full scorecard with sources is in [Benchmark Run #001](https://github.com/roy-tong/AgentMeasure/blob/main/reports/benchmark-run-001.md). If you publish usage numbers, tell us how they're graded. If you have a claim we should audit, send it over — the next run is already scheduled.
