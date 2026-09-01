---
name: research-knowledge-base
description: Search and synthesize Roy.Tong's public AI product research about AI agents, embodied AI, intelligent hardware, product commercialization, and evidence-led industry research. Use for AI product research, embodied AI research, intelligent hardware research, public research notes, finding relevant Roy's Notes articles, comparing published arguments across time, or citing original public pages. 中文触发：检索 Roy.Tong 知识库、AI产品研究、Agent研究、具身智能、智能硬件、商业化产品、行业研究文章。
license: MIT
---

# Roy's AI Product Research Library

Use this Skill as a read-only map to Roy.Tong's published AI product research. It requires network access to `https://roy-tong.github.io` and exposes public reports, data summaries, research notes and articles, not private memory, unpublished Feishu documents, or personal files.

## Workflow

1. Read `https://roy-tong.github.io/llms.txt` first. For reports, data and research notes, use `https://roy-tong.github.io/knowledge/materials.json`; schema 3.0 lists research questions, current views, evidence gaps, material scope, limits, versions, downloads and public text. The legacy `knowledge/index.json` remains available for articles and projects.
2. Select the relevant research dossier to understand the question and evidence gap, then choose only the material pages needed. Open the original page before citing or summarizing it.
3. Label Roy.Tong's analysis as analysis. For claims that require current or primary evidence, follow the article's citations or obtain authoritative sources separately.
4. Preserve publication and revision context. Do not present an older article as Roy.Tong's current position when a newer page revises it.
5. Answer with links to the original public pages and state any gaps. Do not infer private beliefs, employers' confidential information, or unpublished work.
6. Respect access scope: a preview is not full text, an aggregate is not raw data, and a related article is not automatically derived from every material in its dossier. Never fetch private inventories or infer permission to redistribute third-party content.

## Good uses

- Find Roy.Tong's writing relevant to an AI product or embodied-intelligence question.
- Compare how a product or industry judgment changed across published notes.
- Route an Agent to iRead Research Monitor, User Demand Research, or Bilibili Video to Transcript through the public Agent Research Toolkit catalog.
- Build a source-linked brief from public Roy's Notes pages.

## Output contract

Return:

1. the user's question in one sentence;
2. the most relevant public pages and why each matters;
3. a concise synthesis that separates published analysis from external facts;
4. unresolved gaps or newer evidence that should be checked;
5. direct URLs for every cited Roy's Notes page.

If `llms.txt` is unavailable, use `https://roy-tong.github.io/sitemap.xml` and `https://roy-tong.github.io/feed.xml`. Stop if the site is unreachable; do not substitute private local memory.
