---
layout: post
title: "2026 Research Review: Judgments That Hold, and Judgments Still Waiting for Evidence"
date: 2026-10-10 00:00:00 +0800
excerpt: "A year of research across twelve directions kept revealing the same skipped step. This review uses only published, checkable research and explicitly labeled research discussions: thirteen judgments, each with evidence and boundaries."
permalink: /en/notes/research-review-2026/
content_id: research-review-2026
knowledge_topic: product-research
knowledge_units: [agent-measurement, demand-evidence, research-workflows]
lang: en
tags: [Research Review, Product Research]
---

A year of research across twelve directions kept revealing the same skipped step. This review uses only published, checkable research and explicitly labeled research discussions: thirteen judgments, each with evidence and boundaries.

## A year of research, separated into two confidence levels

Over the past year, my research covered twelve areas: camera robots, sports hardware, brain-computer interfaces, AI glasses, home robots, agent measurement, and edge computing. They look unrelated. Put together, they repeatedly show the same leap: a problem is found, so adoption is assumed; a capability works, so delivery is assumed; a log says success, so value is assumed.

This review collects the judgments that can currently stand. It uses two kinds of material: published research you can open and check, and internal cross-analysis explicitly labeled as research discussion. Private project budgets, customers, and schedules are excluded. Every judgment carries its evidence and boundary. Financial data and public audits belong to one confidence tier; discussion frameworks belong to another. They deserve different weight.

## Camera robots: movement is the selling point and the unpaid debt

In 2026, this category set records and kept failing. Beni raised $4.58 million on Kickstarter, reaching 9,169% of its goal. The failure list grew too: Sporttotal entered insolvency, MOVE'N SEE faced liquidation, Snap discontinued Pixy, and Skydio left the consumer market. A working tracking algorithm has never been enough to establish a product.

First, split the category. “Camera robot” covers at least four products: autonomous moving camera positions, robotic camera-movement equipment, fixed AI photographers, and robots that also happen to film. Users buy something different in each. Putting fifteen companies in one competitor table assumes they compete for the same market.

For the first group—the only one selling movement itself—I proposed one standard: the unassisted-session rate, meaning the share of sessions where the user never touches the device and still wants to publish the result. None of the companies whose public material I checked disclosed it. Crowdfunding proves that people can imagine the category. Delivery and retention prove the product.

The strongest counterexample to moving cameras comes from a company that does not make robots. Veo records the whole field from a fixed panoramic position, then uses AI to generate virtual tracking. In fiscal 2025 it reported DKK 593.5 million in revenue, a 62.9% gross margin, and its first full-year profit. Among the companies I checked, the only one that could prove category-level profitability through audited financials was the one whose camera stayed still. Every moving-camera company must answer the same question: do parallax, occlusion relief, and height changes justify the noise, safety, battery, and reliability costs? If an 8K crop can produce the shot, the robot should not move.

## Sports hardware: the strongest signal is the workaround, not AI

The most important finding in sports-hardware research was not a model benchmark. It was a behavioral signal: users have been assembling their own products for years. Japanese players ask friends to occupy adjacent stations and film each other; Korean practice ranges tie phones to chairs; American players combine alignment sticks with phone mounts. These workarounds recur across markets and over time. Users rarely say “I need an AI camera,” but they keep tolerating awkward routines to finish the task. That is stronger evidence of pain than a requested feature. It does not prove willingness to pay.

The first product question is therefore not “what can AI do?” but “where is the greatest friction, and where can we be reliable enough?” In sports recording, the best-supported loop is not an AI coach. It replaces “set up the phone, adjust the angle, start recording, walk back, play, return, stop, find the clip, edit” with “put down the device, play, and find the video ready.” Automatic recording and editing remove an entire workflow. A reliable record may be worth more than a mediocre diagnostic system.

The current validation map: strong problem evidence, moderate support for the solution direction, insufficient evidence for the form, almost no willingness-to-pay evidence, unverified AI-coach PMF, and no retention evidence. The dangerous move is not building the wrong AI. It is adding dual cameras, 360 capture, gamification, and an AI coach before proving payment. The product can be reduced to three jobs: record the right thing, find what is worth watching, and know what to change in the next set. Every other feature earns its place against those jobs.

## Demand research: in a new category, questionnaires measure imagination

The biggest lesson from brain-computer-interface research was methodological. When users lack a stable mental model of the product category, questionnaires and focus groups easily measure imagination rather than behavior. A questionnaire cannot recover an experience the user has never had. Look for evidence where users have already left traces: workaround behavior, purchases, and long-running complaints.

Two disciplines are worth keeping. First, multi-framework ablation: evaluate the same evidence under competing narratives, with only three verdicts—supported, overturned, or insufficient sample. The third is as legitimate as the other two, and the standard cannot be changed after seeing the data. Second, payment evidence gets its own track: attitude and wallet stay separate. Interview interest, a crowdfunding order, and long-term use prove different things. They cannot be stitched into one imaginary complete user.

## Agent measurement: every usage number is self-reported

The agent economy is building badges, comparisons, measurement, and payments on numbers nobody can verify. I audited six real public usage claims. Every number was self-reported, and none published a unit definition. What exactly is “a payment,” “a merchant,” or “an AI request”? None of the six said. At 160 million transactions priced at $0.25 each, an ill-defined unit is no longer an analytical problem. It is a financial-integrity problem.

My response is built into AgentMeasure: evidence has levels, and missing evidence is UNPROVABLE rather than quietly becoming zero. The first public evidence case produced 0%: twelve attempts, 0% safe-operation coverage, with the recalculation script published. The second produced an honest null result: an observed 25-percentage-point increase with p=0.29. The engine did not beautify it. That is why the engine exists. The standard is no longer just a document; it has started producing its own evidence.

## Three gates: the shared pattern across the research

Across twelve directions, the recurring pattern forms three gates. A problem does not imply adoption of your solution. A working capability does not imply complete task delivery. Successful execution does not imply an accepted outcome. Camera robots are queuing at the first gate. Sports hardware sits between the first and third. Agent measurement is repairing the third gate itself. The full argument appears elsewhere; this review lays out the evidence already gathered at each gate.

## Only three things are owed next

Judgments are a safe place for research to stop. A validation list is a more honest one. Next:

1. Camera-robot comparison: in the same scenario, record with a fixed camera, fixed PTZ, and moving camera. Measure which version users choose to publish, not tracking accuracy.
2. Sports-hardware willingness to pay: do not research more features. Find out who will pay to remove the existing friction.
3. Measurement consistency: replicate the “participate → evidence → fix → contribute” loop across the next group of observability and gateway projects.

Each has a failure condition. If the fixed camera wins, the movement narrative needs rewriting. If only coaches respond to the payment test, the recording-loop pricing hypothesis must be downgraded. If the loop finds no real bug in another project, it was luck rather than a loop.

## References

- [From “It Works” to “Worth Using”: Three Gates for AI Products (Chinese)](/notes/ai-product-value-loop/)
- [Camera Robots: Why Must the Camera Move? (Chinese)](/notes/camera-robots-why-must-walk/)
- [A Demand-Research Method for Consumer Brain-Computer Interfaces (Chinese)](/notes/bci-demand-research-method/)
- [Every Agent Usage Number Is Self-Reported](/en/notes/every-agent-usage-number-is-self-reported/)
- [AgentMeasure README, pinned commit](https://github.com/roy-tong/AgentMeasure/blob/67c276b7d17d5a00dc2fa89681eae97f29eeda06/README.md)
- [AgentMeasure: From Specification to Evidence](/en/notes/agentmeasure-from-spec-to-evidence/)
