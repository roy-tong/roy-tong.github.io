---
layout: post
title: "Verovo Charge and Delivery Review: From a Synthetic Example to a Reproducible Acceptance Protocol"
subtitle: "Imagine an AI competitor-research task costing $55, with outdated prices in the final report. That amount explains invoice structure; it is not a test result or supplier quote. Should you check the bill or the delivery first? This synthetic example separates charges, delivery, and evidence, with commands and boundaries."
date: 2026-11-06 00:20:00 +0800
permalink: /en/notes/agent-bill-verification/
content_id: agent-bill-verification
knowledge_topic: agent-systems
knowledge_units: [agent-measurement, evidence-maintenance]
lang: en
tags: [AI Agent, Acceptance, Product Methods]
reading_time: 6
description: "An agent invoice contains more than tokens. A synthetic example separates charge, delivery, and evidence states."
excerpt: "An agent invoice contains more than tokens. A synthetic example separates charge, delivery, and evidence states."
---

Verovo is a tool I built to check AI task charges and delivery. This article uses its built-in synthetic example.

**Key conclusions**

- Agent invoices contain more than tokens: search, browsing, OCR, translation, and storage can be billed per call, page, or minute.
- “Charges passed” does not mean “delivery passed.” “Missing record” does not mean “failed”; it means “unprovable.”
- Acceptance needs two tables: charges cover amounts, rates, and usage; delivery covers task counts, human intervention, and completion evidence.
- This uses Verovo 0.13.0’s built-in synthetic example, not customer data. Commands, outputs, and version appear in the reproduction appendix.

## 1. If the bill is right, is the work done?

AI task acceptance is often compressed into one question: is the invoice correct?

The invoice should be correct. But it covers whether money was calculated according to the rules, not whether the work was completed according to them.

One task can simultaneously have:

- charges passed;
- delivery failed;
- one item that cannot be proven.

A summary color makes “charges passed” look like “task complete.” The three states need to be separated.

## 2. Why an agent invoice is more than tokens

Imagine a competitor-research task. The call volumes and $55 below are invented to explain the structure. They are not a supplier quote or Verovo’s built-in sample.

The task searches 20 competitor websites, opens 50 product pages, OCRs prices from images, translates several English passages, and generates a report.

The month-end invoice might look like this:

| Item | Charge | Billing unit |
|---|---:|---|
| Model tokens | $20 | Per token |
| Search API | $15 | Per query |
| Browser / scraping | $10 | Per runtime minute |
| OCR | $5 | Per page |
| Translation | $3 | Per character |
| Storage / export | $2 | Per GB |

Total: $55. Model tokens are only one line.

Three issues are easy to miss:

1. **Different billing units:** models use tokens, search uses queries, browsing uses minutes, and OCR uses pages. You estimate by task; the supplier charges by call.
2. **Retries may be billable:** a page fails three times, or an empty search leads to another keyword. Whether these are charged depends on the service, failure stage, and pricing rule. Check the logs.
3. **Duplicate calls:** the same page is fetched twice or the same paragraph translated twice. Without deduplication and caching, the invoice inflates.

These differences require both call logs and billing rules. Before assigning work, specify which calls are allowed, their limits, and what happens when the limit is crossed.

## 3. A synthetic example with three states

Verovo’s built-in sample keeps only three items:

- The agreed amount is $100 and local records also show $100: charges pass.
- The delivery rule allows at most two tasks requiring human rescue; records show five: delivery fails.
- An external completion record was not supplied: the report does not guess. It marks the item unprovable.

All three results hold at once.

This is neither “invoice fraud” nor “the AI must be lazy.” It shows that **the charge table and delivery table are different tables.**

| Table | What it checks | Result here |
|---|---|---|
| Charges | Amount, rate, usage, rules | Pass |
| Delivery | Task count, human intervention, completion evidence | Fail |
| Evidence | Completion records, sources, hashes | Unprovable |

“Unprovable” is not “failed.”

A missing record may mean the supplier did not return it, a file was not saved, permission was not granted, or the task was not done. Separate three verdicts:

- Fail: repair, resubmit, or re-review according to the agreement.
- Unprovable: request evidence; do not declare failure without it.
- Pass: rule, record, and receipt are present.

Separating failure from “I do not know” is the easiest step to omit and one of the most valuable.

## 4. Apply it to your own task

You do not need to buy a tool first. Do three things:

**Write the task contract.** Which tools are allowed? How many calls of each type? What is the total budget, retry limit, and maximum number of human rescues? What counts as completion, and where does the evidence live?

**Give every call an ID.** Record task ID, tool name, time, input summary, output summary, and charge. Reconcile the invoice by task ID, not by guessing from the supplier name.

**Build the three-state table.** Pass, fail, unprovable. Do not fill gaps with “should be fine.” Missing evidence stays missing.

A practical sequence:

1. Write charge rules and run once to confirm amounts and rates.
2. Write delivery rules and run once to confirm task counts and human intervention.
3. Add completion records and mark every gap without guessing.

## 5. The tool cannot sign for you

This run verifies whether given rules match given records.

It does not verify:

- whether the rules are reasonable;
- whether the records are authentic;
- whether the contract applies;
- whether to pay, accept delivery, or request remediation.

A hash helps track which files were used. It does not prove the records themselves are true. Missing evidence does not automatically become failure or success; it stays unprovable.

In a real business, the responsible person must decide payment, acceptance, and accountability against the actual agreement.

## 6. Reproduction appendix

### Environment

- Date: November 5, 2026; this run exited with code 0.
- Project: Verovo local source, version 0.13.0; HEAD `4c6ac4bfa2887d63643bced1dc3a70fd699dfd82`.
- Runtime: Python 3.9+. No new PyPI installation was performed, and the run was not inside Doubao, WorkBuddy, or another host.
- Input: project-provided synthetic data, not customer data.

### Command

```bash
python3 healthcheck/verovo review --sample \
  --html buyer-review.html \
  --json buyer-review.json
```

### Output

```text
CHARGES: PASS (1 checks; 0 evidence gaps)
DELIVERY: FAIL (2 checks; 1 evidence gaps)
[UNPROVABLE] delivery / completion-evidence
```

### Failure and recovery

- **Command not found:** confirm you are in the repository root and `healthcheck/verovo` exists.
- **Python version too old:** the README requires 3.9+.
- **Wrong input format:** run `--sample` first, then adapt your JSON to its structure.
- **Report will not open:** the HTML is a local file; open it directly in a browser.
- **Unexpected result:** inspect item verdicts and hashes in the JSON, then the rules and records.

## 7. References

- Verovo 0.13.0 local source and synthetic example.
- [AI invoice reconciliation: seven failure modes](https://github.com/roy-tong/verovo/blob/main/buyer-ledger/docs/ai-invoice-reconciliation.md)—90 synthetic invoice lines, four input buckets plus output, recalculation to cents, and residual items separated.
- [Your AI support invoice counts the resolutions it certified itself](https://roy-tong.github.io/Verovo/blog/resolution-bill-check.html)—a local reconciliation path for resolution-based billing.
