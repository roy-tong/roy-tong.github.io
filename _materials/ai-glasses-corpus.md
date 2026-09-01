---
title: AI 眼镜与开放场景 · 语料汇总
resource_type: data
order: 40
summary: AI 眼镜与开放场景研究的语料范围、平台分布及历史候选标签统计。适合核对样本口径，不用于推断总体市场需求。
reviewed_at: 2026-08-31
version: 2026-08-31 汇总快照
access: 仅汇总数据
source_label: 本站已公开数据汇总
study_id: ai-glasses-2023
use_for: 核对 AI 眼镜与开放场景语料的规模、来源偏差和历史候选标签口径。
scope_note: 209,862 条记录的聚合统计；20 类来源；JSON 与 CSV 汇总。
boundary: 不含原始文本；组合快照不能替代产品反馈子集或真实采用证据。
review_status: 汇总算术、来源合计与公开字段已复核
record_count_label: "209,862"
top_sources:
  - {label: Reddit, records: "174,791", share: 83.29}
  - {label: YouTube, records: "21,279", share: 10.14}
  - {label: VITURE 公开评论, records: "4,734", share: 2.26}
formats: [JSON, CSV]
downloads:
  - label: 下载本组汇总
    url: /knowledge/data/ai-glasses-summary.json
    format: JSON · 本组
  - label: 下载三组对照总览
    url: /knowledge/data/corpus-summary-2026-08-31.csv
    format: CSV · 三组
---

## 这份快照与旧文章不是同一分母

这份组合快照覆盖 2023-01 至 2026-07 的开放场景记录，用于检查来源偏差和历史候选标签。此前文章使用的是更窄的产品反馈筛选集；两者的纳入条件不同，不能用 209,862 替换旧文样本数。

20 类来源并不均衡：Reddit 占 83.29%，YouTube 占 10.14%，VITURE 公开评论占 2.26%。这些比例描述采集结果，不代表设备用户或潜在购买者的分布。

## 机器标签能支持什么

E0–E5 是历史处理产生的候选标签。本轮只复核各标签计数能否加总到总记录数，没有逐条确认发言中的产品、角色、行为和上下文。因此 E3 或 E5 不能直接解释为购买、留存或需求已经成立。

两条记录缺少原有文本哈希字段；“其余哈希未重复”也不是语义去重证明。按规范化后的完全相同文本检查，本组与本地 AI 组共享 104 条，与家庭机器人组共享 72 条。

## 复核到哪里

公开文件允许复算来源、标签与结构质量的汇总关系，不包含正文、平台账户、用户标识和原帖地址集合。记录月份来自字段，不表示各月连续、均匀覆盖；完整边界见[数据方法](/knowledge/data/)。
