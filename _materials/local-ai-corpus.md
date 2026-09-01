---
title: 本地 AI 与个人算力 · 语料汇总
resource_type: data
order: 30
summary: 本地 AI 与个人算力研究所用语料的结构统计，包含记录范围、来源分布和质量检查。仅公开汇总，不含原始用户文本。
reviewed_at: 2026-08-31
version: 2026-08-31 汇总快照
access: 仅汇总数据
source_label: 本站已公开数据汇总
study_id: local-ai-2024
use_for: 核对本地 AI 研究语料的规模、时间范围、来源构成与结构质量。
scope_note: 211,088 条记录的聚合统计；7 类来源；JSON 与 CSV 汇总。
boundary: 不含原始文本；记录数不是人数、市场份额或已验证购买需求。
review_status: 汇总算术、来源合计与公开字段已复核
record_count_label: "211,088"
top_sources:
  - {label: Reddit, records: "190,425", share: 90.21}
  - {label: Hacker News, records: "12,456", share: 5.90}
  - {label: 公开论坛, records: "2,810", share: 1.33}
formats: [JSON, CSV]
downloads:
  - label: 下载本组汇总
    url: /knowledge/data/local-ai-summary.json
    format: JSON · 本组
  - label: 下载三组对照总览
    url: /knowledge/data/corpus-summary-2026-08-31.csv
    format: CSV · 三组
---

## 这份快照固定了什么

快照把本地 AI 与私有算力研究使用的一批记录固定在 2024-01 至 2026-07。公开层保留总量、七类来源的计数、时间字段、结构检查和输入快照摘要；原始帖子、账户、用户标识及逐条文本均未发布。

来源高度集中：Reddit 占 90.21%，Hacker News 占 5.90%。因此它适合发现部署、配置、隐私和持续运行中的问题，不适合估计不同人群的市场比例。

## 分母与跨组重复

211,088 指反馈记录，不是独立用户。主快照没有 E0–E5 编码字段，下游文件中的机器标签不能倒填成原始数据事实。

按 Unicode NFKC、空白折叠和首尾清理后的**完全相同文本**检查，本组与 AI 眼镜组共享 104 条文本，与家庭机器人组共享 133 条。这个检查不包含模糊匹配或人物关联，所以三组记录既不能直接相加，也不能据此宣布完成语义去重。

## 复核到哪里

公开 JSON 与 CSV 可以复算来源合计、比例和结构质量字段；输入摘要通过 SHA-256 绑定到本轮私有快照。本次没有重新爬取，也没有逐条进行语义审核。完整重算仍需要获得原始快照的合法访问权限。
