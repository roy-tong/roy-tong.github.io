# Roy Tong · AI 产品、具身智能与开源研究工具

[访问网站](https://roy-tong.github.io) · [全部文章](https://roy-tong.github.io/archive/) · [iRead](https://github.com/roy-tong/iRead)

这是 Roy Tong（仝夏瑞）的个人网站与长期研究档案，主要记录：

- AI 产品、Agent 与新交互；
- 具身智能、人形机器人和 AI 硬件；
- 从技术机会到产品定义、交付与商业化；
- 开源、本地优先的研究工具 iRead。

## 推荐阅读

- [从 AI 应用到真实世界：我的一次转向](https://roy-tong.github.io/notes/from-ai-software-to-physical-world/)
- [具身智能入门：产业、公司、产品、技术与职业地图](https://roy-tong.github.io/notes/embodied-intelligence-beginners-guide/)
- [重新开始写作](https://roy-tong.github.io/notes/start-writing/)

## 站点能力

- GitHub Pages + Jekyll，无数据库和广告追踪。
- 响应式布局、深色模式、RSS 和语义化页面结构。
- Open Graph、结构化 SEO 信息、sitemap 和明确的 robots 边界。
- 中文系统字体优先，不依赖 Google Fonts，降低首次打开等待时间。

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
