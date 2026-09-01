---
title: 家庭机器人与开放场景 · 语料汇总
resource_type: data
order: 50
summary: 家庭机器人研究的语料规模、来源构成与历史候选标签分布，配合任务与失败恢复笔记阅读。原始平台内容不再分发。
reviewed_at: 2026-08-31
version: 2026-08-31 汇总快照
access: 仅汇总数据
source_label: 本站已公开数据汇总
study_id: home-robots-2023
use_for: 核对家庭机器人研究语料的规模、时间范围、来源集中度和结构问题。
scope_note: 208,755 条记录的聚合统计；6 类来源；JSON 与 CSV 汇总。
boundary: 不含原始文本；机器候选标签不等于人工确认的任务或需求。
review_status: 汇总算术、来源合计与公开字段已复核
record_count_label: "208,755"
top_sources:
  - {label: Reddit, records: "184,008", share: 88.15}
  - {label: Hacker News, records: "19,023", share: 9.11}
  - {label: YouTube, records: "3,581", share: 1.72}
formats: [JSON, CSV]
downloads:
  - label: 下载本组汇总
    url: /knowledge/data/home-robots-summary.json
    format: JSON · 本组
  - label: 下载三组对照总览
    url: /knowledge/data/corpus-summary-2026-08-31.csv
    format: CSV · 三组
---

## 这份快照怎样进入任务研究

快照覆盖 2023-01 至 2026-08 的开放场景记录。它的作用是帮助发现家庭任务、失败情形和替代方案的线索，再回到具体场景做人工判断；它本身不能回答家庭是否愿意长期采用或付费。

六类来源中，Reddit 占 88.15%，Hacker News 占 9.11%。平台讨论的出现频率不能外推为家庭用户分布，也不能替代接管次数、维护负担和长期使用行为。

## 标签与旧报告如何处理

E0–E5 是历史机器处理产生的候选结果。本轮核对了标签合计，没有逐条确认发言所指的产品、角色、上下文及实际行为，因此不沿用旧报告中未经复核的“需求已闭合”结论。

有一条记录缺少原有文本哈希。按规范化后的完全相同文本检查，本组与本地 AI 组共享 133 条文本，与 AI 眼镜组共享 72 条；这不是人物去重或语义去重。

## 复核到哪里

公开层只提供结构汇总、月份范围和输入摘要。原始反馈、个人标识、内部产品方案以及未经授权的第三方内容保持私有。完整方法和可复算层级见[研究数据说明](/knowledge/data/)。
