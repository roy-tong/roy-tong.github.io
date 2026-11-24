---
title: "如何做好 GitHub 开源项目：方法论与工具全景"
resource_type: "report"
order: 72
summary: "把官方指南、开源协作经典、维护者注意力经济、治理与安全实践整理成一套开源项目经营方法。"
reviewed_at: "2026-10-12"
version: "方法论全景 · 2026-10"
access: "全文公开"
source_label: "基于公开方法、公开文档与公开案例的原创整理"
use_for: "检查一个开源项目在定位、文档、治理、社区、安全和长期维护上的缺口。"
scope_note: "方法论与公开案例；不包含私有项目运营数据或未授权社区对话。"
boundary: "方法论不保证项目增长；star、下载与讨论量不能替代真实采用和持续维护。"
review_status: "公开来源可回查；动态排名与案例状态需按日期更新"
formats: "[网页]"
---
- 研究日期：2026-10-11
- 研究方式：四个并行研究员实网查证（①权威方法论 ②增长实战 ③工具资产与 skill 生态 ④实证数据），关键论断附来源 URL，非凭记忆
- 服务对象：开源项目库用途①「学习如何经营 GitHub 项目」；可直接支撑 AgentMeasure 运营
- 证据标注约定：来源括注为一手复盘/官方文档/同行评审论文/行业调查；少数被搜索工具截断到域名级的链接单独注明

---

## 结论速览（TL;DR）

1. **没有现成的「开源项目运营 skill」**：本机 30+ 个技能里没有对口的；社区侧——Anthropic 官方 skills 仓库（19 个 skill）、五个主流 Claude skills 目录（合计收录数万条）、GitHub 按 "open source maintenance skill" 检索——都没有这类 skill。空白是真实的，但蒸馏素材齐全（见第八节），值得自建一个。
2. **方法论本身非常成熟**，六块互补：GitHub 官方 opensource.guide（个人维护者全周期 checklist）、Karl Fogel《Producing OSS》（多人协作机器的运转原理）、Nadia Eghbal《Working in Public》（维护者注意力经济学）、TODO Group（企业 OSPO 视角）、OpenSSF Badge/Scorecard（工程卫生底线）、CHAOSS（健康度度量仪表盘）。
3. **所有方法论的最大分歧**：「多吸收贡献者」（opensource.guide）vs「保护维护者注意力」（Working in Public）。2025-2026 的 AI slop 潮（curl 约 20% 提交是 AI slop、Google 冻结 OSS 漏洞奖励通道至 2027）让天平明显倒向后者。
4. **实证上最硬的几条**：issue 首次响应时长决定新人留存（Zhou & Mockus 2015，IEEE TSE）；star 是注意力指标不是采用指标（Borges & Valente 2018），且假 star 已侵蚀 16%+ 的热门仓库（CMU StarScout，ICSE 2026）；65% 热门项目卡车因子≤2（Avelino 2016）；16% 热门项目被弃置、其中 41% 靠新核心开发者接盘救活（Avelino 2019）。
5. **增长侧被反复验证的打法**：文档先行（文档站建好前不大推）、README 当 landing page、多渠道分日排期把动能在 24-48 小时窗口内打透（Trending 按窗口内 star 增速排名而非总量）、发布日秒回评论、首发扑街后换 messaging 可以再发。
6. **对当前工作**：AgentMeasure 可直接用 GitHub Community Standards + OpenSSF Scorecard 当运营验收清单；本报告可进一步蒸馏成自有 skill。

---

## 一、有没有现成 skill？（调查结论）

| 检查位置 | 结果 |
|---|---|
| 本机技能清单（30+：内容写作/研究/外联/文档办公等） | 无对口 |
| anthropics/skills 官方仓库（180k 星，19 个 skill） | 全是 docx/pdf/pptx/xlsx/前端/API 类，无开源运营 |
| ComposioHQ/awesome-claude-skills（76.8k 星，最大目录） | 分类里无 open source/maintainer/repo 运营条目 |
| travisvn、BehiSecc、seb1n、futantan、helloianneo 等其余四个主流 skills 目录 | 均无 |
| obra/superpowers（社区大 skills 库） | 15 个全是开发流程类（TDD/debugging/code review），无 |
| GitHub 按 "open source maintenance skill" 检索 | 无命中 |

**结论：社区不存在被主流目录收录、拿来即用的「开源项目运营 skill」。** 最接近的替代品是四层组合：

1. **内容层**：opensource.guide（有官方简体中文版 https://opensource.guide/zh-hans/ ）+ 《Producing Open Source Software》中文版（https://producingoss.com/ 站内切中文）
2. **执行层**：GitHub Community Standards 检查清单 + `.github` 默认社区健康文件机制（平台原生、机器可执行）
3. **自动化层**：semantic-release / release-please / Renovate / Dependabot / stale bot / anti-slop 等装完即用的零件
4. **agentic 层（2025-26 新增）**：AGENTS.md、llms.txt、AI 贡献政策

---

## 二、方法论版图：三大学派 + 三个辅助体系

### 2.1 GitHub 官方 opensource.guide —— 个人维护者全周期 checklist

链接：https://opensource.guide/ （GitHub 维护；仓库 https://github.com/github/opensource.guide ，15.7k 星，含简繁中文等 28 种语言）

全部 13 章：参与贡献 / 启动项目 / 寻找用户 / 构建受欢迎社区 / 维护者最佳实践 / 领导与治理 / 获得报酬 / 行为准则 / 指标 / 法律层面 /（新）安全最佳实践 /（新）维护者平衡与自我关怀 /（新）无障碍。

重点章节主张：

- **启动项目**：没有完美时机，标准是「愿意让别人看你的工作并给反馈」；必备四件套 LICENSE+README+CONTRIBUTING+CODE_OF_CONDUCT；命名查商标、预注册域名与社交账号；发布前清查敏感信息；组织开源至少两人有管理权限。
- **寻找用户**：先想清楚解决什么问题；给项目统一主页（Django 联合创始人称建站是早期最对的事）；到受众聚集处（HN/Reddit/SO/meetup/会议）精准发布，「先帮助别人再期待回报」；信任靠时间，没有一夜爆红的捷径。
- **构建社区**：贡献者漏斗的关键是每阶段减少摩擦；文档优先（GitHub 2017 调查：不完整文档是最大痛点）；48 小时内得到代码评审响应的贡献者回头率显著更高（Mozilla 研究）；公开记录一切；零容忍坏行为者；good first issue 迎接新人；冲突时「README 即宪章」。
- **维护者最佳实践**：记录一切（愿景写进 README/VISION 防 scope creep）；「No is temporary, yes is forever」；自动化（测试、semantic-release、dependabot、模板）；允许暂停防倦怠——「维护者的快乐是项目存活的 non-negotiable requirement」。
- **治理**：角色三分 maintainer/contributor/committer；GOVERNANCE.md 写清晋升路径；三模式 BDFL（Python）/精英制（Apache）/自由贡献制（Node.js/Rust），共性大于差异。
- **获得报酬**：热门项目维护每周 10-20 小时；路径：说服雇主、独立筹资、赏金、OpenCollective、付费支持（Sidekiq）、付费托管（Ghost）、基金会；申请资助要能回答五问（影响力/牵引力/对资助方价值/资金用途/接收方式）。
- **指标**：四类——发现（Traffic/stars）、使用（下载/clones）、留存与贡献（首次/偶然/重复贡献者比例）、维护者响应（响应时间是鼓励重复贡献的关键，确认即可不必立即处理）。

### 2.2 Karl Fogel《Producing Open Source Software》—— 多人协作机器

链接：https://producingoss.com/ （第 2 版 CC BY-SA 全文免费，**有官方简体中文版**；正在编写第 3 版）

- **透明三条公理**（第 2 章）：避免私下讨论、显性代码审查、从第一天就开放。
- **书面文化**（第 6 章）：「写作清晰是一个人能拥有的最重要技能之一」；长期看善于沟通者比只善于编程者更能影响项目方向；识别 bikeshed 效应（话题越小争论越长）；安全披露五步流程。
- **commit 权限**（第 8 章）：希波克拉底原则「首先不造成伤害」——最重要的标准是判断力不是技术能力；态度宽松（100 个 committer 里 88 个每年只修错字也好过只有 12 个大拿）；撤销权限是「首先尽量避免的处境」，撤销讨论须私下进行（透明原则的唯一明示例外），但规则与名单必须公开（MAINTAINERS/COMMITTERS 文件置顶）。
- **「信用是自由软件世界的主要货币」**：小贡献被致谢的人会回来做更多。
- **治理**（第 4 章）：forkability 是治理地基——「分叉的可能性正是自由软件项目中不存在真正独裁者的原因」；项目变老会从 BDFL 趋向共识民主（群体治理演化上更稳定，且几乎不会回退）；成文规则「描述协议而非发明协议」，以新人高频问题为准，别写「要有礼貌」这类废话。

适用：严肃的多方参与（企业/基金会）中大型社区项目。

### 2.3 Nadia Eghbal《Working in Public》—— 维护者注意力经济学

链接：https://press.stripe.com/working-in-public （Stripe Press，含免费电子版）；交叉验证：https://blas.com/working-in-public/ 等多篇独立书摘

- **四象限（用户数 × 贡献者数）**：
  - Toys（少×少）：副业实验项目
  - **Stadiums（多×少）：现代最常见形态**（Babel、webpack），核心问题是 curation（筛选）
  - Clubs（少×多）：多数用户即贡献者（Astropy）
  - Federations（多×多）：Rust、Linux，需要正式治理
  - 项目可在象限间迁移（Hadoop 从 stadium 长成 federation）
- **贡献者分层**：maintainers（受托人，keystone species）→ active contributors（动机是社区/声誉/学习）→ **casual contributors**（一次性顺手贡献，交易性动机；类比 NYC 游客：在场≠社区成员。注意术语是 casual 不是 causal——常见误写）。85%+ 的项目中不到 5% 的开发者贡献了 95% 的代码与社会互动。
- **维护成本结构**：现代开源的危机不是代码被过度使用，而是「用户争夺维护者注意力的过度参与使工作难以为继」——维护者的工作本质是 curation 不是最大化参与；GitHub 作为平台把重心从在线社区转向个人创作者，像经纪人一样提供分发；资助结构错配：传统产权解决「首版成本」，维护是重复博弈，成本随时间累积。
- **对 stadiums 的操作主张**：生产与消费分离——单向镜（代码可自由消费、限制消耗维护者时间的渠道）、拒绝 extractive contributions（合并边际成本超过项目收益的贡献）、CI/机器人/模板降低前置成本、甚至 n=1 模式（一个人维护、不收外部 PR）。
- **资助有效性**：有效=patronage（订阅赞助）、边界清晰的赏金、直接资助个人（项目越小越模块化越有吸引力）；无效=补偿 casual contributors（他们的贡献本就供过于求）、paywall、micropayments。

### 2.4 辅助体系

| 体系 | 是什么 | 考核维度 |
|---|---|---|
| TODO Group 指南 | https://todogroup.org/guides/ 24 篇，Linux 基金会，企业 OSPO 视角 | 立项前先攒声誉；只开源「非核心但生产在用」的代码，**绝不能把开源社区当代码倾倒场**；已有类似项目就加入而非造轮子；许可证/CLA 法务审查；甚至有《如何体面关停项目》指南 |
| OpenSSF Best Practices Badge | https://www.bestpractices.dev/ 自认证徽章，passing/silver/gold 三级 | passing 六维：基本信息（FLOSS 许可/文档/HTTPS）、变更控制（版本号+人类可读发布说明）、报告（bug 与漏洞上报流程+响应时限）、质量（自动化测试）、安全（加密算法/60 天修复中等漏洞/不泄凭据）、分析（静态/动态分析） |
| OpenSSF Scorecard | https://scorecard.dev/ 公开仓库自动打分 0-10 | 18 项检查：漏洞/依赖更新工具/持续维护/安全政策/许可证/CI 测试/Fuzzing/SAST/分支保护/代码评审/多组织贡献者/pinned dependencies/token permissions/signed releases 等；2026-04 发布 v5.5.0，活跃 |
| CHAOSS | https://chaoss.community/ 社区健康度量，89 指标+17 模型 | 常用：新人转化率、贡献类型、组织多样性、**Elephant Factor（大象因子：贡献最多组织占比）**、Contributor Absence Factor、burnout/心理安全；工具 GrimoLab/CollectOSS 活跃，2026 新设 AI Alignment 工作组 |

### 2.5 学派间的矛盾与调和（重要）

1. **「多吸收贡献者」 vs 「保护注意力」**：opensource.guide 倡导漏斗/good first issue/给权限；WiP 认为对 stadiums 应单向镜过滤甚至 n=1。调和：**先分象限再选策略**——clubs/federations 用前者，stadiums 用后者；AI slop 潮让天平进一步倒向 WiP。
2. **commit 权限的逻辑**：opensource.guide 当激励（归属感）；Fogel 反对身份化，且附带完整撤销程序。
3. **治理正式化时机**：opensource.guide 主张「观察后再正式化」；TODO（企业）要求立项即明确；Fogel 折中：约定积累到一定量就写下来。
4. **度量的意义**：opensource.guide/CHAOSS 把活动当健康信号；WiP 的稀缺资源是维护者注意力，增长即成本。CHAOSS 的 burnout 指标实际是对 WiP 关切的量化回应。
5. **透明的例外**：Fogel——撤销权限的讨论须私下；安全漏洞与行为准则举报同理。
6. **立场差异**：TODO 站企业（IP/CLA/法务）；WiP/opensource.guide 站个人维护者（倦怠/资助个人）；WiP 引 Evan You：「公司资助的项目一旦不再服务公司目的就会被砍」。

**一句话整合：Fogel 给「怎么运转多人协作机器」，opensource.guide 给「个人维护者全周期 checklist」，TODO 给「企业怎么开源」，Badge/Scorecard 给「工程卫生底线」，CHAOSS 给「健康度仪表盘」，WiP 给「什么时候该少做事而不是多做事」。**

---

## 三、生命周期操作框架

| 阶段 | 各体系强调什么 |
|---|---|
| **0 立项前** | 没有完美时机，先设目标；先参与现有项目攒声誉；只开源「非核心但生产在用」的代码；已有类似项目就加入；想清楚要走向哪个象限（toys 起步，目标 stadium 还是 federation） |
| **1 启动** | 四件套 LICENSE+README+CONTRIBUTING+CODE_OF_CONDUCT；命名查商标；从第一天就公开；Standard Readme 结构、Keep a Changelog、SemVer、all-contributors 从第一天就用（避免追溯成本）；Badge passing 级要求（测试/发布说明/安全政策）当工程底线 |
| **2 找到用户** | 统一主页；到受众聚集处精准发布；「先帮别人」；用发现→使用指标（Traffic/下载/clones）；警惕：用户增长即维护负债的开始 |
| **3 社区/贡献者** | 每阶段减摩擦；48h 首响；good first issue；公开记录；零容忍不良行为；书面文化；**对冲：先判象限——stadiums 的正确动作是 curation 而非「建设社区」**；2025-26 起必须加 AI slop 防御 |
| **4 治理** | 观察后再正式化 vs 立项即明确（视项目性质）；GOVERNANCE.md 写晋升路径；forkability 是地基；共识为主投票为辅；行为准则用 Contributor Covenant 3.0（2025-07 发布）并真正执行；资金选财政赞助方（SFC/Apache/LF/Open Collective） |
| **5 长期维护** | 记录一切、说 No、自动化、防倦怠是「不可协商的存活条件」；SECURITY.md+私密漏洞报告；Scorecard 18 项当体检表；CHAOSS 维护者响应/缺席因子/burnout 指标；**体面退场也是维护的一部分**（README 顶部注明项目状态，TODO 有专门指南） |
| **6（可选）商业化/资助** | 五问框架；商业参与是正常能量来源；open core 的「开多少闭多少」权衡；有效资助=patronage/赏金/资助个人/机构化基金（Sovereign Tech Fund→EU-STF 是 2024-26 主流方向）；无效=补偿 casual contributors/micropayments |

---

## 四、增长 Playbook（冷启动实战）

依据：PHPStan、Wasp×2、Digger 四篇一手复盘 + Dub.co PH 冲榜复盘 + Supabase Twitter 运营分析 + Charlie Marsh（uv）访谈。

### 4.1 发布前（1-8 周）

1. **先验证问题再写代码**：Wasp 做了 25 次问题访谈才动手，第一个里程碑是「确认四大痛点」而不是 100 star；PHPStan 教训：「先做最难的核心功能，纠结名字/域名/首页是拖延」。
2. **README 按 landing page 设计**：Banner→Badges→About 一句话（大白话！差例「flexible polyglot orchestration framework」，好例「a tool to easily integrate widgets」）→视觉 demo GIF→安装→Quickstart（目标是带用户达成第一个小成果）→对比表→Contributing→License；原则「尽量短，细节去文档站」（https://www.markepear.dev/blog/github-readme-guide ）。
3. **GitHub 站内 SEO 独立于 Google**：仓库排名主要看 Name+About 描述+Topics 而不是 README；核心词进仓库名和 About（描述越短关键词占比越高，小仓库可排在 star 多 20 倍的大仓库前面）；Topics 用单词、最多 20 个。
4. **文档站是前置件不是后置件**：Wasp 关键发现——Docusaurus 文档建好后「开发者乱批评的意愿明显下降」，之后 Reddit 才爆发。文档=转化页+长尾 SEO 资产：约 80% 流量在任务级关键词（"How to do X in Y" recipe 页），50 篇 recipe × 50 开发者/月 ≈ 每月 2500 高质量访客。
5. **打磨 messaging 比加功能重要**：Wasp 从「新编程语言」改为「配合 React & Node 的胶水层/less boilerplate」后，Reddit 帖从 20 分扑街变 263/365 赞。
6. **贡献者上手设施**：CONTRIBUTING.md + 预打好 good-first-issue 标签的小 issue（bug 修复、文档改进）+ 入口 issue。别指望新人做大事：Wasp Hacktoberfest 24 个 PR 中 20 个是 xs/s 级。
7. **社区底座与物料**：提前建 Discord、养 X 账号（「发布不是一条推文而是持续分享过程」）；PH 轮播图>视频、首条评论文案、统一短链。
8. **Reddit 账号预热**：6 个月以上、有 karma 的老号；先当贡献者；90:10 法则（90% 有用内容，<10% 提自己项目）；有疑问先私信版主。

### 4.2 发布日

9. **Show HN 写法**：自己的语气像和老同事聊天；禁最高级形容词；结构=团队→一句话说清→为什么难/重要→背景故事→带技术细节的方案→差异点→邀请反馈；**发布后秒回评论**、深挖技术细节、绝不找人灌水、被批评时「先认同能认同的部分」——说服对象是围观者不是批评者（Fly.io 联创一人回 53 条评论）。
10. **Show HN 时机**：周日 06:00 UTC 上首页概率约为周三 09:00 UTC 的 2.5 倍（2018-19 全量数据分析）；2025 年 2.3 万帖分析同样指向周日晚/周一凌晨（太平洋时间）。**共识：比选时点更重要的是发后第一小时守着回评论。**
11. **Reddit**：选对版块——r/opensource、r/SideProject 允许自我推广；r/webdev 只允许周六 Showoff Saturday；最优质转化来自技术栈小版块（r/reactjs、r/golang）；写法=讲带数字的故事（"we cut docker build times by 70%"），身份披露放末尾。Wasp 实测 r/javascript 263 赞 + r/reactjs 365 赞 ≈ 270 stars（单次最大跳涨）。
12. **X/Twitter**：结构=钩子→前两推放 demo GIF→可复制代码→仓库链接→明确求 star。Supabase 反例更有启发：几乎不用长线程，「让缩略图说话」，公告配 meme（不关心功能的人也会转 meme），每条推文必有视觉元素；用 Launch Week 把普通迭代变成事件。
13. **Product Hunt（期望值调对）**：Dub.co 打法=周二至四、提前一周 Teaser、12:01 AM PST 上线、首小时 150 upvotes/50 评论、回复每条评论→日/周/月三榜第一（1085 票/2000+ 访客/663 注册）。但 2025 共识在降温：387 次发布研究显示 PH 转化率约 3.1%，远低于 Indie Hackers 精华帖的 23.1%；对开发者受众 HN/Reddit 常常更好，PH 价值更多是徽章/背书。
14. **多渠道分日排期，不要同一天全发**：Digger 实际顺序=Reddit（r/golang）→YouTube 大 V 直播→周日 Show HN→周一进 Golang trending→周二进全球 Trending。
15. **Trending 窗口逻辑**：Trending 排名的是**窗口期内 star 增速而非总量**——500 star 仓库一天涨 300 可排在只涨 50 的 10 万 star 仓库之上；官方算法黑箱（OSS Insight 因此自建透明榜单）。实操含义：把所有渠道动能在 24-48 小时内集中释放，「连续的小胜利互相放大」。

### 4.3 发布后 30 天

16. **star 请求做成显式 CTA**：文档站顶部提示条（Algolia 做法）、README、推文里直接开口。
17. **向 awesome-xxx 清单提 PR**：读目标清单 CONTRIBUTING 和 awesome-lint 规则（按字母序、单 PR 单条目、描述以句号结尾）；大清单可先开 issue。
18. **长文分发**：dev.to/Hashnode 跨发借官方账号二次曝光；Hashnode 可绑自定义域名保留 SEO 权重。
19. **issue/PR 响应速度=留存**：PHPStan「回应每一个 bug 和 PR」；Digger 强调 trending 靠真实用户 star 增速、刷量不可行（GitHub 2024 底起清理假 star）。
20. **蹭 Hacktoberfest（10 月）拉第一批贡献者**：提前备小 issue、good-first-issue 外加上下文标签（docs/example）、入口 issue、官方 Discord 自荐频道；「只给仓库贴标签不会有人来，营销投入决定回报」。
21. **复盘与再发布**：每个里程碑写复盘长文（复盘本身又成传播素材）；**一次发布失败可以换 messaging 再发**——Wasp 首发仅 20 分，一年后换定位再上 HN 拿 222 分。

### 4.4 持续增长

22. **文档站持续产 recipe**：每个公开 API 至少配一篇 How-to，监控文档页自然落地量、文档→注册转化、「站内搜索零结果」找内容缺口。
23. **版本即事件**：Supabase 式 Launch Week，把功能攒成一周集中发，事前预告事后总结。
24. **生态位设计决定复利**（案例实证）：
    - **shadcn/ui**：「这不是组件库，是你构建自己组件库的方式」——CLI 把源码复制进用户仓库（完全所有权）；registry 模式催生第三方生态，后又成为 AI 编码工具默认输出格式，**传播被写进了分发模型本身**。
    - **uv（Astral）**：入口刻意做成 `uv pip install` 兼容层降低迁移成本，6 个月后才推完整界面；持续投入打包标准解决生态痛点；被 AI 编码代理采用形成正循环，月下载 1.26 亿次——「增长看下载量不是 star」（Charlie Marsh 访谈）。
    - **Ollama**：踩中 2023 中 Llama 2 开源模型爆发点，Docker 式体验 + OpenAI 兼容 API 成为生态默认后端，靠 HN/Reddit 自然增长。
    - **browser-use**：2024 底-2025 抓住 agent 浪潮，演示视频在 X 病毒式传播，数月 50k stars（现 110k+），2025-03 融 1700 万美元，核心 MIT+云服务变现。
25. **指标体系：star 是虚荣指标**：更硬的信号=包管理器下载量、dependents、Docker pulls、forks/clones、活跃贡献者数、文档→注册转化。定位：**star 衡量注意力，下载/dependents/留存衡量采用。**

### 4.5 被反复验证的增长共性（8 条）

1. 没有魔法发布日，只有梯子——首发扑街很正常，换 messaging 再发就能成。
2. 文档先行——文档站建好之前不要大推。
3. README = landing page——一句话大白话价值主张+首屏 demo GIF+一行安装命令+快速上手到第一个成果。
4. 渠道各有性格——HN 吃谦逊+技术细节+秒回；Reddit 吃故事+90:10；X 吃视觉缩略图+直接 CTA；PH 吃重准备但对开发者工具转化一般。
5. 时机在 24-48h 窗口内打透——Trending 按窗口 star 增速排名，多渠道分日排期形成连续动能。
6. 贡献者冷启动靠「小+带路+秒回」——小 PR 的价值是让人成为贡献者，不是清 backlog。
7. 分发模型本身可以是增长引擎——降低迁移成本+让别人能在你之上建生态（shadcn 复制源码/uv pip 兼容层/Ollama OpenAI 兼容 API）。
8. 用使用指标而非 star 衡量成败。

---

## 五、实证数据：什么真正有效

### 强证据（同行评审/平台级数据）

| 结论 | 来源 |
|---|---|
| 热门项目 16% 被弃置；41% 靠新核心开发者接盘救活 | Avelino 等 ESEM 2019（1,932 个项目） |
| 65% 热门项目卡车因子≤2（失去 1-2 人即瘫痪） | Avelino 等 ICPC 2016（133 个项目） |
| star=注意力≠使用/质量，与使用量仅弱相关 | Borges & Valente JSS 2018（被引 500+） |
| 2019-2024 全量检测出约 600 万疑似假 star、18,617 仓库刷星；2024-07 高峰时 16.66% 热门仓库被刷过 | He 等 ICSE 2026（CMU StarScout） |
| 新人首次行动到收到响应的时长显著影响留存 | Zhou & Mockus IEEE TSE 2015（被引 189） |
| 广泛使用的开源价值最高 8.8 万亿美元，约 96% 需求侧价值由约 5% 开发者产出 | HBS（Hoffmann et al. 2024） |
| Copilot coding agent 2025-05 至 09 创建超 100 万个 PR；50% 开源项目至少一名维护者在用 Copilot；同时 commit 评论量下降 27%——评审带宽没有同步增长 | GitHub Octoverse 2025 |
| 5 行以上重复代码块 2024 年增长约 8 倍，重构持续下滑 | GitClear《AI Copilot Code Quality 2025》（2.11 亿行变更） |
| Valkey/OpenTofu/OpenSearch 分叉成功（83% 大企业在测 Valkey；OpenTofu 下载近 1000 万） | LF/AWS/Percona 等多方数据 |

### 中等证据

| 结论 | 来源 |
|---|---|
| README 含贡献指南/外部链接/团队信息与流行度正相关（相关≠因果，更可能成功项目有资源写文档） | Venigalla 2022（1,950 份 README）、Wang 等 JSS 2023（5,000 仓库） |
| 全平台仅约 63% 公开仓库有 README、5.5% 有贡献指南、2% 有行为准则——治理配套普遍缺失 | GitHub Octoverse 2025 |
| 46%-60% 维护者完全无报酬；60% 曾辞职或认真考虑过辞职（自选样本偏差） | Tidelift 2021/2023 |
| 拿报酬的维护者实施关键安全实践的概率高 55% | Tidelift 2024 |
| 约 20 美元的小额赞助反而相对降低创新产出（挤出内在动机） | NBER w31668（准实验） |
| 主动寻求资助的开发者仅约 2/5 实际收到过捐赠 | ICSE 2024 |
| 42.7% npm 包超过两年未更新（单一研究） | Pu 2025 |
| Dependabot 每月开 300-400 万修复 PR，仅约 1/3 当月合并 | Octoverse 2025 |

### 轶事级但密度高的信号

- curl：2025 年约 20% 提交是 AI slop，安全报告一度 6 份仅 1 份为真（Daniel Stenberg 2025-07）；2026-01 直接关停 bug bounty。
- Google 2026-10 因 AI 提交激增**冻结 OSS 漏洞奖励计划产品漏洞通道至 2027**（平台公告级）。
- 英国 AISI 的 Inspect AI 仓库被约 400 个 AI 账号的生成 PR 淹没；Ghostty 改为仅接受受邀 PR。
- 证据缺口提示：issue 响应时间→项目存活的直接回归证据较弱（最强链路是响应→新人留存）；AI slop 占 PR 的精确百分比无权威统计。

---

## 六、2025-2026 新变量（老指南没写的）

1. **AI slop 冲击与防御**：GitHub 2026-02 起征求社区意见提供「关闭/限制公开 PR」的开关（kill switch）与 PR 速率上限；工具层有 peakoss/anti-slop（844 星，GitHub Action，34 条规则自动检测关闭 slop PR）、CodeRabbit triage；freeCodeCamp 试点「检出 slop 即降优先级数日后关闭」；Zig/NetBSD/Gentoo 限制或禁止 AI 生成贡献。**新项目从第一天就该有 AI 贡献政策。**
2. **README 双读者化**：AGENTS.md（https://agents.md/ ，已归 Linux 基金会管理，6 万+ 项目采用，「给代理看的 README」：构建/测试命令、代码约定）+ llms.txt（https://llmstxt.org/ ，站点级规范，2026-08 出 v2）。主流实践=README 给人、AGENTS.md 给 agent。Selenium 2026-09 官方实践：发布 llms.txt 索引 + AGENTS.md 规则文件，让 agent 只学当前文档以减少「以同样几种方式出错」的 AI PR。
3. **许可证钟摆回摆**：宽松许可→2018-2023 转 source-available（Mongo/Elastic/HashiCorp/Redis）→2024-2025 部分回归开源（Elastic 2024-09 加回 AGPL、Redis 8 2025-05）。2026 行业共识：**AGPL 成为「新的防御性开源默认」**（过法务又能约束云厂商）；分叉赢了且原厂回不了头（Valkey/OpenTofu/OpenSearch 三案）；「基础设施选型现在是治理决策而不只是技术决策」。
4. **治理反面教材**：WordPress/WP Engine 冲突（2024-09 Mullenweg 封锁 WP Engine 访问 WordPress.org 并接管其插件；法院 2024-12 发初步禁令）——「名义社区基础设施实为个人控制」的治理风险。
5. **资助机构化**：德国 Sovereign Tech Fund 模式 2025 年被推动扩展为欧洲 EU-STF；GitHub Secure Open Source Fund 持续为关键安全维护者付费。
6. **维护者用 AI 减负**：Copilot Code Review 用户 72.6% 认为提升评审效率；Autofix 使漏洞修复提速 3 倍+（1.5h→28min）。AI 既是冲击也是减负工具，双向都在加速。

---

## 七、可直接复用的资产清单

### 7.1 机器可执行的运营基线（GitHub 原生）

- **Community Standards 检查清单**（Insights→Community）：README、License、Code of Conduct、Contributing、Security policy、Issue 模板、PR 模板、ACCESSIBILITY.md（新）、SUPPORT.md、good first issue 标签。https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions
- **`.github` 特殊仓库**：账户名下建 `.github` 公开仓库，社区健康文件自动成为全部仓库默认值（改一处全账户生效，不污染 Git 历史；LICENSE 除外）。https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file

### 7.2 自动化工具/机器人

| 工具 | 解决什么 | 链接 |
|---|---|---|
| all-contributors bot | 评论一条命令自动生成 README 贡献者 emoji 表格（认可非代码贡献） | https://allcontributors.org |
| semantic-release | 分析 conventional commits 自动定版本/生成 changelog/发布 | https://semantic-release.org |
| release-please（Google） | Release PR 人在回路模式，支持 20+ 语言和 monorepo | https://github.com/googleapis/release-please |
| release-drafter | PR 合并自动起草 Release Notes，最轻方案 | https://github.com/release-drafter/release-drafter |
| Renovate | 跨语言依赖自动更新，可调度降噪 | https://docs.renovatebot.com |
| Dependabot | GitHub 原生依赖+安全+Actions 更新 | https://docs.github.com/en/code-security/dependabot |
| actions/stale | 自动标记关闭长期无活动 issue/PR | https://github.com/actions/stale |
| CodeQL | 代码扫描引擎，default setup 一键开 | https://docs.github.com/en/code-security/code-scanning |
| Artifact Attestation | 构建产物签名溯源 | https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations |
| anti-slop | 34 条规则自动检测关闭 AI slop PR | https://github.com/peakoss/anti-slop |

### 7.3 模板与生成器

contributing-gen（CLI 生成 CONTRIBUTING+CoC 骨架）、Standard Readme（6.4k 星，规范+生成器+徽章）、choosealicense.com（官方选许可证向导）、FUNDING.yml（11+ 赞助平台）、Issue Forms（YAML 表单式模板，减少低质量 issue）、shields.io（徽章事实标准）。

### 7.4 元资源（含中文）

- opensource.guide 简体中文版：https://opensource.guide/zh-hans/
- 《开源软件之道》（Producing OSS 中文版）：https://producingoss.com/ 切中文
- 开源社（Kaiyuanshe，OSI 中国首个官方合作伙伴）：《中国开源年度报告》 https://kaiyuanshe.github.io
- InfoQ「社区运营」专题：OpenMLDB、PingCAP 等国内实操长文
- 知乎经典问题「如何运营一个开源项目并取得较大影响力」（2017 起）
- checklist 仓库：cfpb/open-source-checklist（687 星）、afonsopacifer/open-source-checklist、eddiejaoude/open-source-repo-checklist

---

## 八、对当前工作的适配建议

1. **AgentMeasure 直接落地**：以 Community Standards 十项 + OpenSSF Scorecard 当运营验收清单（机器可查）；增长 playbook 里最先值得做的是——文档站先行、README 重构成 landing page（一句话大白话+demo GIF+一行安装）、GitHub 站内 SEO（About/Topics 关键词）、发布日多渠道分日排期。对应 AgentMeasure 现有 `运营/`、`市场推广/` 目录可直接引用本报告。
2. **开源项目库的方法论层补齐**：宽表里的 100+ 研究对象可加两个标注维度——生命周期阶段（本报告第三节七阶段）与四象限类型（stadium/club/federation），让案例库与方法论互查。
3. **与出名目标联动**：开源项目是媒体体系的素材源与可信度资产。四个候选方向里**评测层天然 GitHub-native**——leaderboard/benchmark 型项目传播性强（对标 LMSYS Chatbot Arena 的分发逻辑），且与「资料型内容涨粉最有效」的账号洞察一致。
4. **值得自建 skill**：社区空白+四层素材（内容/执行/自动化/agentic）已齐，可蒸馏一个「开源项目运营」skill：触发词如「开源项目运营」「launch 开源项目」「仓库体检」；验收标准直接复用 Community Standards 清单。建议用 skill-creator 流程做，内容边界=本报告第二、三、四、七节。

---

## 九、主要来源索引

**方法论**：opensource.guide（https://opensource.guide 及仓库）· producingoss.com · Working in Public（press.stripe.com/working-in-public，书摘 blas.com/working-in-public）· todogroup.org/guides · bestpractices.dev · scorecard.dev · chaoss.community

**增长一手复盘**：PHPStan 0→1k stars（phpstan.org/blog/how-i-got-from-0-to-1000-stars-on-github-in-three-months-with-my-open-source-side-project）· Wasp 1000 stars（wasp.sh/blog/2022/09/29/journey-to-1000-gh-stars）· Wasp Hacktoberfest（wasp.sh/blog/2022/11/17/hacktoberfest-wrap-up）· Digger trending（medium.com/@DiggerHQ/how-we-got-into-github-trending-c281f3b06df9）· Dub.co PH Playbook（dub.co/blog/product-hunt）· Markepear 系列（markepear.dev/blog）· Charlie Marsh 谈 uv（pydevtools.com/blog/charlie-marsh-test-set-interview）· OSS Insight（ossinsight.io/blog/introducing-trending-page）

**实证论文**：Avelino 2019（arxiv.org/abs/1906.04821）· Avelino 2016（ICPC）· Borges & Valente 2018（arxiv.org/abs/1811.07643）· He et al. ICSE 2026（arxiv.org/abs/2412.13459）· Zhou & Mockus 2015（IEEE TSE）· Venigalla 2022（arxiv.org/abs/2206.10772）· NBER w31668 · Tidelift 2021/2023/2024 · Octoverse 2024/2025（github.blog）· GitClear 2025（gitclear.com）

**AI 冲击与 2025-26 动态**：Daniel Stenberg "death-by-a-thousand-slops"（daniel.haxx.se/blog/2025/07/14）· The Register（GitHub PR kill switch，2026-02）· TechCrunch（Google OSS VRP 冻结，2026-10）· Selenium 官方博客（2026-09）· agents.md · llmstxt.org · flowverify 2026 relicensing 复盘（flowverify.co/blog/open-source-relicensing-2026-what-happened）

> 注：少数二级来源被搜索工具截断到域名级（Syften、Ask HN 线程、freeCodeCamp 论坛帖等），已在正文注明；核心结论均有一手来源支撑。
