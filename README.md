# Roy.Tong · 把前沿技术转化为可商业化的产品

[访问网站](https://roy-tong.github.io) · [个人知识库](https://roy-tong.github.io/knowledge/) · [Agent 索引](https://roy-tong.github.io/llms.txt) · [全部文章](https://roy-tong.github.io/archive/) · [iRead](https://github.com/roy-tong/iRead)

[![Agent Skill](https://img.shields.io/badge/Agent_Skill-research--knowledge--base-111111)](skills/research-knowledge-base/SKILL.md)
[![skills.sh](https://skills.sh/b/roy-tong/roy-tong.github.io)](https://skills.sh/roy-tong/roy-tong.github.io/research-knowledge-base)

这是 Roy.Tong 的个人网站，首页按“定位 → 文章 → 开源项目 → 关于与联系”组织，主要记录：

- AI 产品、Agent 与新交互；
- 具身智能、人形机器人和 AI 硬件；
- 从技术机会到产品定义、交付与商业化；
- 从前沿技术到可商业化产品的方法；
- iRead Research Monitor、User Demand Research、Bilibili Video to Transcript 与公开研究知识库等开放能力。

## 给 Agent 使用

知识库按六个长期问题组织：Agent 与软件系统、具身智能与机器人、AI 终端与新交互、创作工具与数字制造、产品研究与商业判断、组织建设与产业落地。第一版连接 20 个知识单元、36 页文章（含 10 页英文译文）与 4 个项目；原有文章链接保持不变。

- [全文索引 JSON](https://roy-tong.github.io/knowledge/index.json)：主题、类型、语言、正文与关联关系。
- [数据与边界](https://roy-tong.github.io/knowledge/data/)：三组研究语料的审查后汇总，不再分发原始平台用户内容。
- [来源台账](https://roy-tong.github.io/knowledge/sources/)与[修订记录](https://roy-tong.github.io/knowledge/changes/)。
- [维护与发布说明](docs/knowledge-maintenance.md)：新增知识、文章、数据与验证方法。

网站提供符合 `llms.txt` 约定的公开内容索引，以及一个只读 Agent Skill：

```bash
gh skill install roy-tong/roy-tong.github.io research-knowledge-base --agent codex --scope user
```

或者使用会公开匿名安装数的 skills.sh CLI：

```bash
npx skills add roy-tong/roy-tong.github.io --skill research-knowledge-base -g -a codex -y
```

Skill 只读取公开文章，不包含私人 memory、未公开飞书文档或本地文件。skills.sh 安装数用于衡量安装，`gh skill search` 关键词排名用于衡量可发现性；两者都不等于实际调用次数。

## 推荐阅读

- [空间计算需要自己的“触控时刻”](https://roy-tong.github.io/notes/spatial-computing-touch-moment/)
- [RAG 之后，Agent 需要 Context Recommendation](https://roy-tong.github.io/notes/agent-context-recommendation-after-rag/)
- [家庭机器人为什么技术上更难，经济上可能更丰富](https://roy-tong.github.io/notes/home-robots-harder-richer/)
- [机器人不是替代人，而是给人增加新的身体](https://roy-tong.github.io/notes/robots-give-people-new-bodies/)
- [空降管理者如何从职位合法性走向组织合法性](https://roy-tong.github.io/notes/appointed-manager-organizational-legitimacy/)
- [Geek、Professional、B、C：不同市场负责消灭不同不确定性](https://roy-tong.github.io/notes/market-roles-remove-uncertainty/)
- [AI Wearable 的竞争，不是眼镜对耳机](https://roy-tong.github.io/notes/ai-wearable-modalities-body-comfort/)
- [竞品分析为什么不该从参数表开始](https://roy-tong.github.io/notes/competitive-analysis-software-hardware/)
- [AI Native 之后，产品的基本单位变了](https://roy-tong.github.io/notes/ai-native-basic-unit/)
- [Agent 向左，具身向右：AI 在信息空间与物理世界的分岔](https://roy-tong.github.io/notes/agent-left-embodied-right/)

## 站点说明

- GitHub Pages + Jekyll，无数据库和广告追踪。
- 响应式布局、深色模式、RSS 和语义化页面结构。
- 中英文核心页面：首次访问时参考浏览器首选语言，页头也可手动切换；网站会记住选择，不调用第三方 IP 定位服务。
- 提供 Open Graph、结构化 SEO 信息、sitemap 和 robots.txt 规则。
- 优先使用中文系统字体，不依赖 Google Fonts，减少首次加载时间。

## 发布文章

在 `_posts` 目录中新建 `YYYY-MM-DD-英文标题.md`：

```yaml
---
layout: post
title: "文章标题"
subtitle: "可选副标题"
date: 2026-07-20 12:00:00 +0800
tags: [AI, 产品]
reading_time: 6
excerpt: "显示在首页和搜索结果中的摘要。"
---
```

提交到 `main` 后，GitHub Pages 会自动构建并发布。文章正文、配图和引用版权由作者负责。

本地预览：

```bash
bundle install
bundle exec jekyll serve
```

发布前运行 `bundle exec jekyll build` 和 `python3 scripts/verify_knowledge.py`。全文检索在浏览器中完成，搜索词只保存在 URL fragment。JavaScript 不可用时，主题和完整文章目录仍可阅读。
