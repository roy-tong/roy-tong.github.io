# 研究资料库维护与发布

第三版把资料库分成私有来源、研究档案和公开资料三层。文章是选择性使用资料形成的下游表达，不计入资料数量。首页以研究问题为入口，档案同时维护当前判断、已有材料与待补证据；`/knowledge/library/` 承担完整目录与全文检索。

## 内容位置

- `_materials/*.md`：已经允许公开的报告、数据和参考清单说明。每项必须有真实正文或可用入口。
- `_knowledge/*.md`：既有研究笔记，保留所有 URL 和正文。默认 `resource_type: note`。
- `_data/research_collections.json`：研究档案的问题、状态、当前判断、材料覆盖、待补证据，以及资料、笔记和文章映射。
- `_data/research_material_types.json`：类型的唯一名称与顺序。
- `knowledge/materials.json`：由正文和研究档案关系生成的公开资料全文索引。
- `knowledge/index.html`：研究档案首页；不承担全量资料检索。
- `knowledge/library.html`：完整公开资料目录、筛选与搜索。
- `knowledge/index.json`：兼容保留的旧综合索引，仍包含既有笔记、文章、项目。
- `_data/knowledge_topics.json`：保留原六领域目录及旧链接；不再作为首页的唯一组织方式。
- `_data/essay_knowledge.json`：原文章与笔记的关系，不必批量改写文章。
- `_posts/`、`en/_posts/`：文章与译文；独立报告已在 `papers/`、书籍介绍在 `book-pages/`。
- `_data/research_sources.json`：公开来源的角色与范围。
- `_data/research_corpora_20260831.json`：原有固定数据快照；不覆盖。
- `knowledge/data/`：数据说明与下载。三份按语料拆分的 JSON 来自同一个公开汇总源。
- `assets/js/knowledge-search.js`：原生 JavaScript 搜索、研究档案/类型筛选、排序、分享筛选状态与加载更多。

私有来源台账、编辑清单与未批准原文在站点仓库之外的个人主页项目工作台。不要放进公开 Git，`published: false`、前端隐藏和 .gitignore 都不是已提交文件的保密机制。

## 新增资料

先核对权属、可见性和完整性，再在 `_materials/` 新增稳定文件名：

```yaml
---
title: 一份具体资料的标题
resource_type: report
order: 80
summary: 这份资料包含什么，读者可以用来做什么。
reviewed_at: 2026-08-31
version: v1.0
access: 全文公开
source_label: 已确认可公开的原创研究
use_for: 这份资料适合回答什么问题。
scope_note: 具体公开正文、试读、汇总还是索引。
boundary: 不能从这份资料外推什么。
review_status: 版本和事实复核到哪里
formats: [网页, PDF]
downloads:
  - label: 阅读报告
    url: /assets/downloads/approved-report.pdf
    format: PDF
---
```

这是字段示意，不要把不存在的示例附件作为真实文件提交。类型允许 `report`、`data`、`reference`；既有笔记用 `note`。

说明页至少写适用问题、当前开放范围、来源/时间、不能外推的内容、复核状态与引用方式。报告可以直接保留原结构，不要求先提炼知识单元或改写文章。对于已经发布的正文，可以设置 `source_page` 指向其原地址；全文索引使用原正文，不复制维护。

在 `research_collections.json` 的 `materials` 中登记文件名。每份资料至少属于一个研究档案，可以进入多个档案但总数只计一次。使用 `notes` 关联旧笔记。新增档案还需增加一个 `layout: research-collection` 的入口页。

内容日期代表材料版本，不用目录收录日期伪装成新研究。新日期数据文件保留旧版本，说明替代关系。只有完整阅读和事实检查真正完成，才可以使用“已核验”一类状态。

## 文章与资料

文章继续使用真实发表地址，`research_collections.json` 中的 `articles` 只列已存在的文章 URL。文末“相关研究资料”说明它们是同题关联，直接证据以正文引用为准。

不要因为一篇旧文章和一份新笔记讨论同一问题，就声称旧文章由新笔记派生。明确核对的引用或派生关系应记录对应资料、版本和正文位置。译文不作为另一份研究证据。

原 `related_posts` 可以连接文章或已经迁移为独立页面的报告；模板及验证脚本都需要解析两者，不能静默丢掉报告链接。

## 数据与公开边界

资料类型、修订状态和可见性分开。数据可以处于原始、清洗、编码、汇总或人工复核阶段，每项说明具体层级。

本批只迁移既有公开汇总，不上传原始平台内容、个人标识、账户链接、逐条文本哈希、企业内部计划或服务凭据。以后如需开放原始数据，需先确认许可和隐私处理；“爬取到”不等于“可以重新分发”。

数据资料必须有字段、单位、分母、时间、来源、处理方法、偏差和可复算范围。机器标签不得当作人工需求验证。来源 PDF、Markdown 或多版本数据不能简单相加为独立资料或用户数。

## 搜索与无脚本使用

全部资料行由 Jekyll 预先渲染。JavaScript 可用时启用即时标题/简介搜索，再加载公开正文；即使索引加载失败，目录和标题/简介筛选仍可用。无脚本时显示完整资料和真实研究档案链接。

筛选状态只存 URL fragment。研究档案、类型和排序支持浏览器返回；输入关键词不会为每个字符制造历史记录。文本从已渲染内容与同源索引读取，不动态插入索引提供的 HTML 或链接。

初始显示 12 份，可继续显示全部。状态区播报匹配数与是否使用完整正文，不能把索引加载失败伪报为“没有资料”。

## 构建与校验

标准环境：

```bash
bundle exec jekyll build
python3 scripts/verify_knowledge.py
python3 scripts/verify_library.py
```

本机已装 Jekyll 3.10 与所需插件，但缺少完整 github-pages bundle；本地可以使用现有运行时：

```bash
ruby -rjekyll -e 'Jekyll::Commands::Build.process({"source" => Dir.pwd, "destination" => File.join(Dir.pwd, "_site")})'
```

本地构建成功不代表已部署。检查唯一资料 ID、真实链接与下载、研究档案及文章关系、索引正文、数据一致性、canonical/sitemap/RSS 和敏感文件排除；在浏览器检查搜索、复合筛选、空状态、清空、返回、手机与深色模式。

不增加仅为凑覆盖率的实现镜像测试。验证侧重点是跨文件合同、回归链接和公开边界。

## 发布与回退

先形成具体发布包：允许公开的说明、正文/附件、来源和版本清单。资料整理不自动授予上传原始材料的权限。

发布前核对远端 main 和未提交修改。只暂存本轮经过检查的文件，不强推、不覆盖他人修改。页面改版与新增私有原稿的发布授权分开处理。

第三版已于 2026-09-01 发布。页面改版不授权公开新增私有原稿；具体资料仍按发布包逐项核对。发布后核对线上内容，回退使用正常还原提交并保留历史。
