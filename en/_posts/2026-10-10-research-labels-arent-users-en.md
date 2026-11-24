---
layout: post
title: "Two Hundred Thousand Discussions Still Cannot Tell You Who Will Buy"
date: 2026-10-10 10:00:00 +0800
permalink: /en/notes/research-labels-arent-users/
content_id: research-labels-arent-users
knowledge_topic: product-research
knowledge_units: [demand-evidence, research-workflows]
lang: en
tags: [Product Research, Research Methods]
reading_time: 7
excerpt: "A pull request enters the data pipeline as a code contribution and leaves as a user asking for help. The problem lives in the meaning the label adds."
---

## What does a record become after processing?

A pull request adding an integration to an open-source project became a “user support request” after data processing.

The developer submitted code. The spreadsheet cried for help on their behalf.

This happened in a local-AI research dataset. The category field was called `support_issue`, which reads clearly enough: someone used the product, hit a problem, and asked for help. But the original record was a code change.

The distinction is worth following through the files. The master snapshot checked on October 10, 2026 had 211,088 rows, including 2,092 from GitHub. Every GitHub row carried the same `support_issue` label. By link type, 598 rows pointed to pull requests. The same count appeared in the labeled downstream view.

This is not a sample of the whole internet. It is a line-by-line scan of specified local files. Rows are not users, and a PR is not worthless. But if “support issue count” is used to discuss purchasing barriers, the category merges different activities into one deceptively precise metric.

## The label adds a meaning the original did not contain

Following the records back to the script reveals a very direct rule: if the source platform is GitHub, return `support_issue` by default. The master build then checks dates, text quality, and topic relevance, and removes duplicates. The current rule does not separate PRs from issue reports at this stage.

The problem is not a lack of cleaning. The dataset went through considerable processing. The problem is that the pipeline converts a source identity into a behavioral identity: coming from a technical platform becomes a user asking for help. A judgment is missing between those two claims.

The AI-glasses research contained a similar rule. Five keyword-hit records checked in a targeted review were still present in the master data, including tester recruitment, product ideas, and sales descriptions. These materials may help explain supply, developer interest, or market conversation. They do not automatically tell us where a user encountered difficulty.

## Balancing months does not fix the role of a record

The edge project also stored a month-balanced view. It had 121,786 rows, including 1,395 from GitHub and 352 links to PRs. Every GitHub row still inherited `support_issue`.

Monthly balancing addresses time distribution: a dominant month can drown out other periods. Record role addresses meaning: is this statement a usage experience, feature proposal, development action, or promotion? Adjusting the month does not change what a sentence is.

Cleaning therefore cannot be judged only by how many rows remain. For the question an article wants to answer, we need to know which categories are still mixed together. PRs can be valuable for analyzing a developer ecosystem. For analyzing user barriers, they first need to be identified separately, then checked for attributable real-world problems.

## Removing PRs still does not produce buyers

Even after all 598 PRs are removed from support-issue statistics, the remaining 1,494 issue links cannot automatically be called 1,494 user pain points. An issue can contain a suggestion, project plan, tutorial, or syndicated news. One real failure can also appear in several duplicate reports.

More fundamentally, someone willing to install a local model is not necessarily willing to buy dedicated hardware. A compatibility error does not mean they want a hardware solution. The conclusion should stop at the layer the original evidence supports.

I prefer to follow the concrete experience: what was the person trying to finish, what did the problem cost, how did they work around it, did they keep using the product, and who paid the cost of resolution? When the record cannot answer these questions, turn them into interview questions. This reduces the number of “needs” available for the report, but brings the remaining material closer to a product decision.

## Report numbers have versions too

An earlier expanded-source report recorded 210,581 rows in the master data. The current file scanned on the same day had 211,088. That difference alone does not prove the old report was wrong, nor that every added record is valid. It shows why a report needs an explicit relationship to a data snapshot.

Combine the sample composition of an early report, the total from a later dataset, and labels from the latest classifier, and every item may be individually true while sharing no common statistical basis.

A practical rule is to attach the file hash, calculation script, and filters to every statistic used in an article. Readers do not need every engineering detail, but the author should be able to answer: which version of the material produced this sentence?

## The research asset worth preserving

This review did not manually label every GitHub record or complete the same audit for other sources. It cannot overturn the entire study. What it can establish is how the support-issue label is generated and how it persists in specified downstream files.

The next step is to separate platform source from content role, then semantically review records tied to specific article claims. After correcting the statistics, check which arguments actually depend on these counts. Claims that do not depend on them need not be discarded merely to demonstrate caution.

The next time I see “200,000 pieces of user feedback,” I will ask: in how many is a user actually describing their own experience?

That is a much smaller question. It is also much harder to answer.

One step further is the layer most often skipped in demand validation: what people say and what they do are different evidence. Askovo’s [need-validation guide](https://roy-tong.github.io/Askovo/guides/need-validation.html) makes this explicit. A verbal statement is E1. Reaching “validated” requires at least one E2: an observed workaround, alternative, or failure. A cell without evidence reads “unknown,” not “zero.”

## Data note

This article reviews local snapshots from personal research material, checked on October 10, 2026. The master data, labeled view, and month-balanced view overlap and must not be added together. Numbers count rows, not people. A PR link identifies a record type; it does not make the record worthless.

The [public counts and methodology](/assets/data/research-label-audit-20261010.json) provide six view summaries, calculation conditions, and full-file hashes. Original platform text, user identifiers, and internal paths are not public. The aggregate can verify the numbers in this article, but cannot independently rerun the full corpus. This classification issue does not alter the historical snapshots or overturn findings from other sources.
