---
layout: post
lang: en
title: "AgentMeasure Weekly: The Spec Is Growing Evidence"
subtitle: "v0.2.0 → v0.2.2 — an open experiment engine, the first preregistered A/B on a real agent, the first external fixture, the first public evidence case, and an honest 0%."
date: 2026-08-25 14:20:00 +0800
reading_time: 8
tags:
  - agent
  - measurement
  - conformance
  - capability economy
description: "Engineering and evidence progress from Aug 22–25: AgentMeasure Lab v0.4 (open experiment engine), the first preregistered controlled A/B on a real agent harness, v0.2.2 conformance hardening with the first community-contributed fixture (Urusilla-001), the first public evidence case (langfuse demo traces: 12 attempts, 0% safe operation coverage), and the spec's move from a ladder to two states plus ranked evidence."
permalink: /en/notes/agentmeasure-from-spec-to-evidence/
---

> The first AgentMeasure progress report. Project: [github.com/roy-tong/AgentMeasure](https://github.com/roy-tong/AgentMeasure), website: [roy-tong.github.io/AgentMeasure](https://roy-tong.github.io/AgentMeasure/). Every number below comes from reproducible run output — no hand-transcribed figures.

## What shipped this week

The project moved from "specification documents" to an "evidence flywheel." Four release nodes, one through-line: **every claim must be recomputable.**

**v0.2.0 (Aug 22)** — Whitepaper v0.3 (EN + zh-CN) + **AgentMeasure Lab v0.4**, an open experiment engine: enforced preregistration, balanced blocked assignment, budget circuit breakers, honest statistics (Wilson intervals, two-proportion tests, honest nulls), and a bilingual decision-maker one-pager in every report. 78 tests.

**v0.2.1 (Aug 22)** — **The first preregistered controlled A/B on a real agent** (codex CLI against a real MCP tool server): 4 tasks × 2 variants, full-funnel capture, real token metering (188K–215K tokens per operation). The result is an honest null: +25pp observed but p=0.29, next round needs ≈31 per arm. The engine did not flatter it — that is the point of the engine.

**v0.2.2 (Aug 24)** — Conformance hardening. The first external conformance pass (from [langfuse discussion #16383](https://github.com/langfuse/langfuse/discussions/16383)) exposed two real bugs: the validator skipped root-level required fields after an `oneOf` branch matched (#8), and the aggregator trusted declared operation summaries without reconciling the underlying attempt rows (#9). Both fixed — and, per the commitment made then, **the first community-contributed fixture (Urusilla-001) was accepted into the conformance suite**. CI now runs external-fixture guards plus the full lab suite on every relevant change.

**Aug 25** — **The first public evidence case** (`conformance/evidence/langfuse-demo-traces/`): Langfuse's published demo seed data (three real framework-instrumented traces, commit-pinned, source not redistributed) run through the canonical pipeline via a disclosed one-off adapter. The result is a 0%:

- 12 attempts, operation grouping evidence **100% missing**;
- **safe operation coverage 0%** — in both fail-closed and structural-experimental modes;
- token usage absent from the export entirely (0/26).

This is not a "our bar is high, everyone else fails" flex. It pins the claim boundary: **these numbers describe these three traces only**. The reproducible scripts (`fetch_source.py` + `run_case.py`, stdlib only) ship with the case — anyone can recompute it.

## The spec revision: from a ladder to two states

The same week, two independent external reviewers (direct replies, anonymous pending consent) read the spec and **independently converged on the same critique**: in my original four-level consumption ladder, `referenced` is not a semantic state — it is a weak estimator for influence with two named failure modes: **cite-without-use** and **use-without-cite**.

The spec is now revised as DR-005, "two states + ranked evidence":

- **availability** (a context fact): whether a capability entered the agent's context;
- **influence** (a behavioral fact): whether it changed the agent's behavior — answered at the experiment layer.

A third reviewer added the provider-side inference boundary: client-side telemetry certifies `serialized-as-sent`, one step short of `reached-inference`. That boundary is now in the definitions.

Also shipped: **M3 execution-grain vectors** operationalizing DR-006 — a runtime retry chain (429 → timeout → success under one `operation_id`) resolves to **1 operation** in the spec, with M3.3 attempt success 0.333 and `attempts_per_operation = 3` forced as disclosure — not three counts of "usage."

**Two experts converging independently is behavioral validation of the spec's direction. Writing it in beats any marketing copy.**

## Product and growth reality

The concurrently released PRD v0.5 records the dual-hypothesis test now in flight: A (conformance toolkit — real external pull already) vs B (usage integrity audit — closer to revenue, unvalidated), with a preregistered four-branch gate review on Sep 3.

One channel, falsified: **cold email.** 616 delivered → 1 meaningful reply → 0 integrations. Closed.

One loop, validated: **structured upstream participation.** One issue in langfuse → the first external conformance pass → two real bugs (#8/#9) → fixed and released as v0.2.2 → the first community-contributed fixture. That participate → evidence → fix → contribute loop is the single most valuable outcome of the week.

The website's trial entry ([roy-tong.github.io/AgentMeasure](https://roy-tong.github.io/AgentMeasure/)) is now dual-path: email-first, GitHub issue as the fallback — the audit's audience is CEOs and CFOs, and they should not be forced to open a GitHub account.

## What's next

- Sep 3: dual-hypothesis gate review (four-branch decision criteria preregistered);
- Lab M2 open-source release and conformance vector completion (execution / reporting layers);
- Replicate the upstream-participation loop on the next batch of observability / gateway / runtime projects;
- Show HN: three of four gates passed; one 2-minute demo short.

One sentence for the week: **the standard is no longer just a document — it is producing its own evidence.**
