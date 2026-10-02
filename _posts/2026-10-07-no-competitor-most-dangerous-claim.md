---
layout: post
title: "「没有竞品」是最危险的竞争分析结论"
subtitle: "否定性研究无法证明不存在；方法的核心是给「暂时没找到」划一条可审计的边界。"
date: 2026-10-07 10:00:00 +0800
lang: zh-CN
reading_time: 6
tags: ["研究方法", "竞争分析", "AgentMeasure"]
description: "第一份竞争报告的结论是：这个品类没有人占据。第二份报告把它推翻了——TareCount 就在做我想做的事，同一个锚点案例、同一套本地运行方案，明码标价 2500 美元一次完整审计。两份报告我都没有删：…"
permalink: /notes/no-competitor-most-dangerous-claim/
---

第一份竞争报告的结论是：这个品类没有人占据。第二份报告把它推翻了——[TareCount](https://tarecount.com) 就在做我想做的事，同一个锚点案例、同一套本地运行方案，明码标价 2500 美元一次完整审计。两份报告我都没有删：合在一起比任何一份单独看都值钱，前一份记录我怎么在铺好的搜索面里穷尽，后一份演示这个搜索面怎么漏、一个写过头的结论怎么被抓出来、写回方法。

竞争分析里最危险的结论就是「没有竞品」。危险在于它听起来像一份证明——拿到的人会照它排产品路线、写融资材料。而否定性研究永远无法证明「不存在」，能证明的只有一件事：在定义好的搜索空间和时间点内，没有找到。第一份报告的原文结论是「品类是空的」，它把这两句话之间的距离一步跳了过去，翻车就翻在这一跳上。

背景是我为自己的开源项目 [AgentMeasure](https://github.com/roy-tong/AgentMeasure) 做 V2 竞争调研。V2 要回答的问题一句话：AI 客服已经按「解决的对话数」计费，而「解决」由卖家自己认定，买家能不能独立验证账单。竞争分析因此面对一个极端问题——这个品类里还有没有人做。这个问题没有直答的路，能交付的最好东西，是一份带边界的穷尽记录。「如何确认品类是空的」这条路不存在，方法真正要解的问题只有一个：怎么给「我暂时没找到」设一条可审计的边界。

## 一、搜索面铺三层：代码、机构、市场

我把搜索面铺成代码、机构、市场三层，每层单独取证。

| 层 | 查了什么 | 结果 |
| --- | --- | --- |
| 代码 | GitHub 全网仓库搜索（API 检索，2026 年 9 月） | `resolution recount`、`zendesk resolution audit`、`zendesk ai resolution billing`、`ai support billing reconciliation` 均为 0 结果；唯一沾边的查询只返回 [Intercom_FRI](https://github.com/Hasnain91169/Intercom_FRI)——0 star、无许可证，README 自述「每个质量指标都是 Claude 打的分，没有标注真值」，性质是求职作品。四家厂商的官方 GitHub 组织（intercom、zendesk、salesforce、hubspot）可检索的数百个仓库里，也没有一个审计工具 |
| 机构 | 13 家点名机构，加标准体系 | Holistic AI、BABL AI、Credo AI、Saidot、Trustible、Fairly AI、ORCAA、Eticas、ForHumanity、IEEE CertifAIEd，法律侧 Mayer Brown、Lexology，外加唯一做过对账动作的 3LI Global——全部只做治理、偏见、合规，没有一家碰账单上的「结果」。ISO/IEC 42001 是管理体系、ISO/IEC TS 25058 是质量评价指南、IEEE 3777 还在立项、NIST AI RMF 是风险管理、COPC 定义人力客服指标：没有一份标准把 "confirmed resolution" 定义成计费级度量 |
| 市场 | 结果计费的普及速度，对买家侧审计数量 | Salesforce 2026 年 6 月签下约 36 亿美元收购 Fin 的[最终协议](https://investor.salesforce.com/news/news-details/2026/Salesforce-Signs-Definitive-Agreement-to-Acquire-Fin/default.aspx)，Fin 4 亿美元年化收入里约 1 亿来自按解决计费；Zendesk 重构为 [Verified Resolutions](https://support.zendesk.com/hc/en-us/articles/9570369117338-About-automated-resolution-tiers)；HubSpot [0.50 美元一个已解决对话](https://www.hubspot.com/company-news/hubspots-customer-agent-and-prospecting-agent-now-you-pay-when-the-task-is-complete)；Intercom Fin [0.99 美元一次](https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes)，客户沉默即按「假定解决」计费。第一轮定义好的搜索面内，没有找到独立的 outcome-billing 审计产品 |

市场层再补三个数字说明痛的量级：一位买家手工审计 40 张工单，账单口径 40% 解决率、逐条核对后 12.5%（[Intercom 社区帖 10516](https://community.intercom.com/fin-product-feedback-member-group-49/fin-s-flawed-resolution-assumption-10516)）；另一位买家报告确认解决率 6–7%、假定解决率近 60%（[社区帖 8268](https://community.intercom.com/analyze-fin-93/how-do-you-improve-your-confirmed-resolution-rate-8268)）；Supportman 的抽样里，256 个对话无客户回复、无引用文章，全部被记为解决（[supportman.io](https://supportman.io/fin-audit/)）。三层合起来，是我在定义好的搜索面内的穷尽记录：代码里没找到、机构里没找到、市场在狂奔而审计缺位。这份记录说的是这三张网上没有捞到东西，不是海里没有鱼——第一份报告把后半句也写进了结论，那是翻车的起点。

## 二、给每个「没找到」划一条可审计的边界

一个只写「没找到」的 0 结果，读者分不清是全世界真没有，还是我没找对地方——这个分不清，正是「没有竞品」这个结论危险的地方。所以每个 0 结果旁边要钉三样东西：**查询词、时间、搜索面**。

第一份报告约 35 次独立搜索，负结果按这个格式记录：`"outcome audit" AI agent vendor pricing startup`（无产品）、`"resolution verification as a service"` 精确短语（无结果）、`AI agent invoice audit` 与 `verify AI agent outcome billing`（无结果）、`ISO standard AI agent evaluation SC 42` 与 `"confirmed resolution" definition standard AI support`（无标准）。换成任何人的手，同样的词、同样的面，应该得到同样的「没有」——得到不一样，说明该更新结论了。

搜索面的边界也要交代。我的记录固定留一节「访问限制」：Zendesk 帮助中心对抓取返回空壳（后来用它的 JSON API 才读到全文）、cio.com 和 lexology.com 对我的 IP 返回 403、Intercom 社区是 JS 渲染的单页应用，抓取的 21 个候选帖里只有 1 个拿到完整正文。这些内容划定结论的适用范围：我只在写明的边界内为「没有」负责，边界之外一个字都不多说。

## 三、最像的对手在同结构里，不在同品类里

铺完三层，搜索面还欠一块：结构相同、品类不同的公司。它们今天不在你的竞争格局里，翻一条产品线就是。

最大的一个是 [Vaudit](https://www.vaudit.com/)，做 AI token/API 账单审计：已独立核验 40 亿美元以上的卖家支出、追回超过 1 亿美元、57 家以上企业客户；2026 年 3–6 月从 60 家公司 3400 万美元的 AI 支出里找出约 170 万美元计费错误，约 5%（[案例页](https://www.vaudit.com/post/ai-billing-reconciliation-how-vaudits-tokenaudit-found-1-7m-in-billing-errors)）；收费是审计额度的 1%；平台清单里已经有 Salesforce。它的产品负责人 Deepak Kumar 的表述，和我的产品定义几乎逐字相同：每个卖家都在给自己的作业打分，买家只能接受分数；任何卖家控制计量表的支出品类，都会长出这个问题。

同结构的还有 [Inferock](https://github.com/inferock/inferock-bench)——本地代理逐 call 验证 LLM 计费，141 star、Product Hunt 当日第一，同样发布了自己的开放标准。再放大一圈：货运账单有 Freehand、恢复审计有 PRGX、电信有 Araxxe、法律 e-billing 有独立审计，广告验证被 [Isara](https://www.isara.ai/blog/the-doubleverify-for-ai/) 引用为先例时已是 48.2 亿美元的市场。在我这轮对照到的成熟支出审计品类里，AI 客服的「解决量」至少还没有形成同等成熟的独立审计层。

还有一个反向信号同样要记录：至少五个独立方公开讲过同一个论点——Clelp 的博客（2026 年 7 月）、3LI 的文章（2026 年 8 月）、Vaudit 的产品负责人、Inferock 的 README、QEval 的 VERDICT 方法，外加两篇 2026 年 9 月的 arXiv 论文（其中[一篇](https://arxiv.org/abs/2609.07680)的实验：只读智能体自报报告的问责层，找回真实故障源的概率 4.1%，低于 20% 的随机基线）。被多方独立表述的缺口是已知缺口，洞察不构成护城河。这行字必须写进竞争结论，否则结论在自欺。

## 四、转折点：搜索面本身会漏

第一份报告的原文结论是：「没有任何公司出售『按结果计费的结果审计』，品类是空的。」它并非一无所获——找到了 Supportman（Intercom 单平台的买家侧 QA，被标为最大战略风险）、做手动对账服务的 3LI、自称只证记录不证诚实的 Glacis。它漏掉的是 TareCount。

漏的原因现在看很清楚：TareCount 是一个人手动跑的服务，免费抽查加 2500 美元一口价完整审计，全部网络足迹是一个落地页和一个 1 star 的仓库。没有融资新闻、没有目录条目、没有搜索排名——我用品类词搜，没有一面搜到它。

第二份报告换了入口，从需求现场找：把 community.intercom.com 站点地图里全部 10,364 个帖子 URL 拉下来，关键词过滤出 71 个候选、抓取 21 个。结果就在锚点投诉帖的评论区里——TareCount 的创始人 2026 年 8 月 2 日和 4 日发过两条评论，向投诉的买家推销免费抽查。早期的竞对不上品类词的榜，它们直接站在鱼最多的池塘里。

这一步是整个方法的关键转折。三层证据、35 次查询，每一条 0 都钉了查询词和时间，但没有一条能覆盖 TareCount——它根本不在那些搜索面上。三件套解决的是 0 可以被复跑，解决不了搜索面本身的盲区：品类搜索没找到，不等于不存在。穷尽只能做尽已知的面，做不出未知的面；未知的那部分，要换入口去现场找。

我后来翻旧笔记，还发现 TareCount 这个名字更早就在一份底稿里出现过一行——「已存在，未计入」。线索来过，被我当成脚注放走了。

## 五、把纠错写进方法

第二份报告的处理方式，是这件事里我最想留下来的部分。它没有悄悄改掉第一份，改在方法注记里写明：竞争报告「品类为空」的结论是错的，它漏掉了 TareCount，以本报告的竞对章节为准。第一份原样保留，两份并排——**错误路径本身就是数据**。

纠错之后还有一步：用同一套怀疑去审计新找到的竞对。TareCount 自称发布了开放标准 ARS-1（CC BY 4.0 草案，2026 年 8 月 27 日），我去验证它的公开足迹：唯一被引用的载体是一篇无法访问的 LinkedIn Pulse 文章，唯一的公开仓库是那个 1 star 落地页——没有对账引擎、没有标准文本、没有许可证。ARS-1 在我的记录里因此降级为「未验证」。找到一个竞对不是终点，它只是把否定性证据的方法换了个对象。

现在我再写「没找到竞品」这类结论，报告固定带三件东西：一张负面证据登记表（查了什么、在哪查、什么时候、没查到什么）、一节访问限制、一个专门的反问——如果它存在但还没有搜索足迹，它会出现在哪个现场。「没找到」是一个带时间戳的观察，随时会过期；按会过期的东西来写它，比按属性来写它准确。

这套方法守不住「没有竞品」，也不打算守。它守住的是每一个「没找到」都有边界、有日期、可复跑。以后谁再给你一份写着「这个市场没有竞品」的报告，先问三个问题：查询词是什么，什么时候查的，搜索面铺到了哪里。三问答得上来，它是一份带保质期的观察记录；答不上来，它只是把「我没找到」写成了「不存在」。
