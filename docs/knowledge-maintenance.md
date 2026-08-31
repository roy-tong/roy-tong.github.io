# 知识库维护与发布

当前公开结构：六主题、20 个知识单元、26 篇中文文章、10 页英文译文、4 个关联项目。首版日期 2026-08-31。英文译文按页面计数，不是独立文章或独立证据。

## 内容位置

- `_knowledge/*.md`：按问题组织的知识单元。
- `_data/knowledge_topics.json`：六主题、入口与关联关系。
- `_data/essay_knowledge.json`：旧文章与知识单元的映射；保留旧文件与 URL。
- `_posts/*.md`：中文文章；英文译文仍在 `en/_posts/`。
- `_data/knowledge_projects.json`：公开项目入口与能力范围。
- `_data/research_sources.json`：公开来源、角色、适用范围与复核日期。
- `_data/research_corpora_20260831.json`：不可覆写的首批数据快照。
- `knowledge/`：目录、主题入口、数据说明、方法与修订记录。
- `assets/js/knowledge-search.js`：浏览器本地全文检索。
- `scripts/verify_knowledge.py`：构建后只读检查；Python 3.9+，无第三方依赖。

页面分工（2026-08-31 第二轮起）：首页是目录页，只列主题问题、单元数与起点，不平铺单元；主题页承载该主题的单元列表与相关项目；单元页承接判断正文。页底折叠的完整目录是无脚本与机器可读的全量入口，新增页面后需保持其链接完整。检索表单在索引就绪前保持禁用（`data-kb-pending`），就绪后由脚本启用。

原始研究资料不放在本仓库。不能用草稿标记、前端隐藏或 gitignore 来为已经提交的敏感文件补救；公开文件必须在进入仓库前审查。

## 新增知识单元

使用稳定英文文件名，发布后不随标题修改而改 URL。前置信息示例：

```yaml
---
title: "一个明确的问题"
topic: product-research
order: 40
reviewed_at: 2026-08-31
summary: "这一页帮助读者作出什么判断。"
related: ["demand-evidence"]
related_posts: ["/notes/scene-user-demand-evidence-research/"]
source_ids: ["sure"]
---
```

正文保留当前判断、依据、成立条件、反例与下一步验证。没有统一证据时应写“作者提案”或“待验证假设”，不以确定语气代替核验。

`related` 引用知识单元文件名，不带扩展名。`related_posts` 使用真实 permalink。`source_ids` 在来源台账中必须存在。模板与检查脚本会验证关联。

## 新增文章

沿用既有 post front matter，补充：

```yaml
knowledge_topic: creative-tools
knowledge_units: ["video-production", "software-capabilities"]
source_ids: ["otio"]
```

旧文章使用 `essay_knowledge.json` 映射，不必为了接入知识库批量改写其正文。历史观点可由新知识页修订；若原文有事实错误，应另加有日期的更正说明。

新文章需完成事实与表达复核，引用原始来源，注明情境示例。不要虚构作者经历、客户案例、实验结果或产品经营数字。

## 数据发布

只加入经过内容与权限审查的汇总。每个新版本使用新日期文件，保留旧快照，记录统计单位、分母、时间范围、来源偏差、去重方法和复现限制。

不得上传原始平台全文、账户标识、个人级链接清单、企业内部资料或任何凭据。本轮只有文件级输入摘要，不包含逐条用户内容哈希。

## 构建与验证

标准环境：

```bash
bundle install
bundle exec jekyll build
python3 scripts/verify_knowledge.py
```

若环境已经装好 Jekyll 3.10、jekyll-feed 和 jekyll-seo-tag，但缺少完整 github-pages bundle，可仅用于本地检查：

```bash
JEKYLL_NO_BUNDLER_REQUIRE=true jekyll build
python3 scripts/verify_knowledge.py
```

该替代检查不等于 GitHub Pages 部署成功。发布后还要核对部署状态与线上实际内容。

检查覆盖索引与关系、页面标题及 canonical、sitemap、内部链接和锚点、旧文章回链、RSS、CSV/JSON 一致性、无脚本目录与敏感路径/凭据模式。自动检查不替代语义、版权与隐私复核。

在浏览器检查桌面与手机尺寸、浅色/深色、中文关键词、主题和类型筛选、空结果、清空与键盘焦点。查询保存在 URL fragment，不上传服务器。

## 发布与回退

只暂存已检查文件，先核对远端 main。不要 force push 或覆盖他人提交。推送后确认知识库首页、全文索引、数据文件和新文章已部署，再宣布上线。

需要回退时，用有说明的正常还原提交处理具体发布变更；不要重写整个仓库历史。敏感数据泄露不能仅靠普通回退解决，应另行处置访问和历史。

## 后续顺序

先提升已发布单元的证据质量，再扩大目录。优先补可公开且可重复计算的案例、任务级人工复核及数据说明。避免把相近版本的报告逐份转成重复文章。
