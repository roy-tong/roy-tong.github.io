# Roy's Notes

Roy 的个人网站，基于 GitHub Pages 与 Jekyll。

## 发布一篇新文章

1. 在 `_posts` 目录中新建 Markdown 文件，文件名格式为 `YYYY-MM-DD-英文标题.md`。
2. 在文件开头填写：

```yaml
---
layout: post
title: "文章标题"
subtitle: "可选的副标题"
date: 2026-07-19 12:00:00 +0800
tags: [AI, 产品]
reading_time: 6
excerpt: "显示在首页的简短摘要。"
---
```

3. 在 `---` 下方使用 Markdown 写正文并提交。GitHub Pages 会自动更新网站。

## 本地预览

如已安装 Ruby 与 Bundler，可运行：

```bash
bundle exec jekyll serve
```

也可以直接提交到 GitHub，等待 Pages 构建完成后查看线上效果。

