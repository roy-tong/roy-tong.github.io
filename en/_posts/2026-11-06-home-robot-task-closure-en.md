---
layout: post
title: "How 200,000 Robot Discussions Become a Product Judgment"
subtitle: ""
date: 2026-11-06 00:10:00 +0800
permalink: /en/notes/home-robot-task-closure/
content_id: home-robot-task-closure
knowledge_topic: robotics
knowledge_units: [household-robots, demand-evidence]
lang: en
tags: [Embodied AI, Home Robots, Product Research]
reading_time: 9
description: "Two hundred thousand robot discussions can reveal whether a task closes, but not a demand rate. Separate the denominator, evidence level, and scenario."
excerpt: "Two hundred thousand robot discussions can reveal whether a task closes, but not a demand rate. Separate the denominator, evidence level, and scenario."
---

You are planning a home robot and receive a dataset of 200,000 discussions. The tempting move is to rank demand by mentions: cleaning is largest, so build cleaning; humanoids are hot, so build a humanoid. That skips two questions: who is speaking, and does the text contain actual usage?

For a product manager, data should help decide whom to find next, what to test, and what to defer. This article follows those decisions to show how public discussion becomes a testable product judgment.

## 1. Know what you are counting

The research retains 208,755 public discussion records from January 2023 through August 2026. One person can post many times, and one post can receive many replies. Records are not users.

There are 44,288 records tagged as robot vacuums and 2,595 tagged as humanoids. Form is multi-label: one record can mention both, and many discuss scenarios or the industry without naming a form. The full set cannot be called 200,000 usage reviews of home robots.

This distinction changes the next step. To study dirty-water-tank maintenance, find experience with existing products. To study whether a humanoid saves work at home, find continuous trial records. A large total cannot substitute for either material.

## 2. Two record types cannot form a purchase funnel

| Rule label in this sample | Robot vacuum | Humanoid |
|---|---:|---:|
| Price or purchase-intent signals | 2,134 | 358 |
| Self-reported purchase, ownership, or usage signals | 1,289 | 4 |

The tempting mistake is to divide the second row by the first and report “conversion rates” of 60.4% and 1.1%. These are not the same people moving through a funnel. There is no user matching, purchase time, or observation window.

“I bought it” is a self-reported purchase, not proof of six months of use, repurchase, or recommendation. The original rules use purchase, ownership, and usage keywords to find candidates; every record has not been manually verified.

The counts still have a use. The 1,289 records are a lead pool for finding real robot-vacuum users and checking maintenance, returns, and continued use. The four humanoid leads show that home-use evidence is thin in this sample and trials should come next. They guide research investment, not conversion or category maturity.

## 3. Translate labels into questions, not capabilities

Two misreadings are common.

**A keyword hit is not automatically a pain point.** The original screening puts clean, wash, and hair in a cleaning-maintenance group. “Clean” may mean “it cleans well,” not “cleaning the machine is hard.” The original 32.1% therefore cannot become “32.1% of users complain about maintenance.” To learn whether maintenance affects continued use, separate mention, complaint, behavior, and consequence, then review a sample.

**Scenario co-occurrence is not product capability.** Among robot-vacuum ownership and usage signals, 535 records also carry household-cleaning tags, 44 elder-care tags, and 37 fetch-and-return tags. “I bought my parents a robot vacuum, but they still need someone to fetch things” can produce several tags. It does not prove the vacuum provides elder care or fetches objects.

These problems call for different actions. Keywords help find the original text; the text reveals who encountered which difficulty, what they do now, and what it costs. Only a clear task, behavior, and person belongs in the product discussion.

Do not attach a feature to every label. “Bought it for my parents” may reveal a division of responsibility among buyer, user, and maintainer. “Failure recovery” asks who intervenes after an interruption. That is closer to the problem than adding an “elder mode” or another smart button.

## 4. Humanoids should be compared on combined tasks

Robot vacuums and humanoids are not one category. Comparing them is useful because it shows how household labor shifts, not because their mention counts should compete.

A robot vacuum mainly replaces floor cleaning. A humanoid’s additional value should appear when it completes several tasks in one bounded scenario: recognizing, sorting, picking up, and putting away objects in a living-room reset. Demonstrating those actions separately does not prove they can happen consecutively.

Divide user time into setup, supervision while the device runs, intervention after failure, and cleanup. Record what the person must do between tasks. If every switch requires rearranging objects, issuing new instructions, and changing tools, several skills may not produce a more convenient product.

Current reviews lack observation of consecutive tasks in one home. Scenario tags cannot replace that test. “No usage signal found” does not mean the capability does not exist in reality.

## 5. Take the research into the next trial

Choose one group and scenario, such as a dual-income family resetting the living room in the evening. Write down the current labor and equipment as the baseline. Run the robot through the same tasks and keep the entire recording: completion, intervention points, recovery time, and cleanup work.

If one action is faster but setup for the whole process grows, fix the process. If every task switch needs human intervention, fix switching and recovery. If performance is stable but the user will not run it again, revisit frequency, noise, space, and maintenance.

Public discussions help choose the question. Continuous use helps judge the product. The next time you receive a large-sample report, find the conclusion that most affects the decision. Is it based on something said, something done once, or one user’s experience over time?

## 6. Reproduction appendix

### Inputs and fields

- Strict sample: `strict_master_2023plus.jsonl.gz`, 208,755 records.
- Key fields: `product_form` (list), `demand_evidence_level` (E0–E5), `corpus_role`, `scene_labels`.
- Data window: January 1, 2023 through August 16, 2026.
- Review date: November 5, 2026. No new collection or source-file changes.

### Coding map

| Statement in the text | Code |
|---|---|
| Scenario context | E0 |
| Task or pain point | E1 |
| Existing alternative | E2 |
| Accepted solution | E3 |
| Purchase intent or price discussion | E4+ |
| Rejection or negative purchase signal | E4- |
| Self-reported purchase, ownership, or usage | E5 |

### Review script

```python
import gzip, json
from collections import Counter

forms, ownership_candidates = Counter(), Counter()
total = 0

with gzip.open("strict_master_2023plus.jsonl.gz", "rt", encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        row = json.loads(line)
        total += 1
        forms_in_row = row.get("product_form", [])
        if isinstance(forms_in_row, str):
            forms_in_row = [forms_in_row]
        for form in set(forms_in_row):
            forms[form] += 1
            if row["demand_evidence_level"] == "E5":
                ownership_candidates[form] += 1

print("records", total)
for form, count in forms.items():
    print(form, count, round(count / total * 100, 2), ownership_candidates[form])
```

Differences between the old report and this recount: robot vacuum 44,150 → 44,288; humanoid 2,534 → 2,595; robot dog 1,097 → 1,133; companionship 2,791 → 2,806; robot-vacuum ownership/usage 1,285 → 1,289. These come from data versions and label recalculation, not new collection.

### Known limitations

- Reddit accounts for 88.1%; Chinese text for about 0.6%.
- Thirteen of 19 quality checks passed; six failed.
- No independent human gold standard.
- Rule coding is not a record-by-record interview conclusion.

Source: general embodied-intelligence household-scenario research, data through August 16, 2026; recounted locally on November 5, 2026.
