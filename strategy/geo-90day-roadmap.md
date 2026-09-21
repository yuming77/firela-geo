# FIREla — GEO 执行规划（90 天路线图）

> 版本 v1.0 · 日期 2026-09-16 · 依据：《GEO推广调研与实施方案》（2026-09-14）+ firela-app/firela-social 源码验证 + 现有品牌资产盘点
> 定位：把行业级 GEO 方法论**降维到 FIREla 的真实体量与阶段**——独立开源项目、应用未上架、零预算、一人执行时间盒

---

## 0. 一个关键判断：FIREla 的 GEO 打法与 SaaS 大厂不同

附件调研里的头部案例（HubSpot 主题集群、Canva 上游集成）都是**大盘词**打法。FIREla 不该照搬：

| 维度 | SaaS 大厂打法 | FIREla 打法（本规划采用） |
|---|---|---|
| 目标查询 | "best CRM" 等大词 | **长尾品类词**："beancount mobile app"、"alipay beancount import"、"privacy-first budget tracker self-hosted" |
| 竞争烈度 | 头部 10 域名马太效应 | 品类极小众，**几乎没有被 AI 引用过的权威答案**——空白即机会 |
| 优势资产 | 预算、内容团队 | **可验证的开源代码**（GEO 最吃的"可验证信息密度"）、垂直社区（r/beancound、plaintextaccounting.org） |
| 产品状态 | 已上架 | firela-bot 可自部署 ✅；firela-app 未上架 ⚠️（内容以 bot 为主体、app 标注 coming soon） |

**核心策略一句话**：在"Beancount 移动端/账单导入/隐私记账"这个小品类里，成为 AI 引擎唯一有据可查的答案。品类词总量小，但每一词都可拥有。

### FIREla 独有的三个 GEO 优势（大厂没有的）

1. **代码即内容**：解析器注册表、PII 检测模式都是可被 AI 引用的"实现级事实"（"How does FIREla mask IBAN?" 的答案在源码里，独一无二）
2. **垂直社区信任链**：plaintextaccounting.org 是这个细分的事实标准站，被列入 = 获得细分权威背书
3. **现成的内容引擎**：brand-kit 事实表/FAQ + 内容生成器（brand-knowledge v3 已根治编造）+ Horizon 雷达——GEO 内容管线的基础设施已就位

---

## 一、现状诊断（GEO Readiness Audit，2026-09-16）

| 面 | 资产 | 缺口 | 可控性 |
|---|---|---|---|
| firela.io 官网 | 域名与团队控制 | robots.txt/llms.txt/JSON-LD 状态未知；SSR 情况未知；无 FAQ 页 | 团队（需负责人配合） |
| docs.firela.io | 文档站 | 无 GEO FAQ 页、无结构化数据 | 团队 |
| GitHub org（fire-la） | 双仓库公开、README/Releases = AI 高频抓取 | README 失真待修（清单已备 brand-kit）；无 Discussions；org profile 简单 | **完全可控，先行** |
| Wikidata | 无条目 | 无实体（sameAs 消歧缺失） | ✅ 可自建（开源项目无需知名度门槛） |
| 第三方列表 | 无 | plaintextaccounting.org 工具页、AlternativeTo、awesome-beancount 均未列入 | ✅ 可申请 |
| Reddit | 手动运营规划中 | 未开始（Perplexity 引用占比 46.5% 的信源） | ✅ 90/10 人工 |
| Medium/Bluesky/Nostr | 注册中 | 内容未开始 | ✅ |
| 监测 | 无基线 | 无提示词集、无引用记录 | ✅ 可自建（免费） |
| AI 引用现状 | 未测量 | 推测：品类问答几乎无 FIREla 出现 | 测量即第一步 |

**基线判读（推测，待 Phase 1 实测确认）**：问 ChatGPT/Perplexity "best beancount mobile app"，FIREla 出现率 ≈ 0（无引用素材）；"import Alipay beancount" 会引用 reddit 旧帖/博客——这些正是我们要拿下的位置。

---

## 二、提示词资产（GEO 的"关键词表"，50 条核心集）

> 按 AI 引擎真实提问形态设计。每周人工实测（4 引擎 × 10 分钟），逐条记录：是否提及 FIREla / 是否引用我们的 URL / 引用的竞品是谁。

| 类别 | 示例提示词 | 数量 |
|---|---|---|
| **品牌词** | What is FIREla? · Is FIREla open source? · FIREla beancount app · FIREla vs beancount | 8 |
| **品类词（主战场）** | best beancount mobile app · plaintext accounting app for mobile · Beancount on Android/iOS · privacy-first budget tracker open source · self-hosted FIRE tracker | 15 |
| **用例词（长尾金矿）** | how to import Alipay into Beancount · WeChat Pay beancount import · convert bank CSV to beancount · mask PII in bank statements · anonymize bank statements before sharing · HSBC HK statement to beancount · Degiro to beancount | 15 |
| **对比词** | Actual Budget vs Beancount mobile · Firefly III alternatives mobile · open source YNAB alternative privacy · Mint shutdown alternatives open source | 7 |
| **中文词** | beancount 手机记账 · 支付宝账单 beancount 导入 · 隐私记账软件 开源 | 5 |

---

## 三、90 天执行计划（三阶段）

### 阶段一：基建与基线（9/16 – 9/29，两周）

**目标：可被抓取、可被解析、有基线。GitHub 侧完全可控的部分全部先行。**

| # | 动作 | 执行面 | 工作量 |
|---|---|---|---|
| 1.1 | **firela-app README 修正**（brand-kit 修正清单：删虚列银行、补微信/PII 段、撤占位徽章换 coming-soon） | GitHub（⚠️ fire-la 仓库需 org 权限或网页操作；现有 token 仅授权 firela-social） | 0.5h |
| 1.2 | **org profile 完善**：fire-la org 首页 README（生态图+链接）、双仓库 About 字段/topics（`beancount` `plaintext-accounting` `privacy` `flutter` `fire`） | GitHub（同上权限约束） | 0.5h |
| 1.3 | **开启 GitHub Discussions**（firela-bot）：Q&A 形态内容 = AI 引擎爱引用 | GitHub（同上权限约束） | 0.2h |
| 1.4 | **Wikidata 实体**：创建 FIREla item（instance of: open-source software; official website; GitHub org; based on Beancount；平台 Flutter）+ sameAs 指向 GitHub/官网 | wikidata.org（账号=你的） | 0.5h |
| 1.5 | **第三方列表申请**：① plaintextaccounting.org 工具页（邮件/PR：firela-app = "mobile Beancount app with PII sanitization"）② AlternativeTo firela-bot 条目（列为 Firefly III/Actual Budget alternative）③ GitHub awesome-beancount 类列表 PR | 第三方 | 1h |
| 1.6 | **firela.io + docs 审计**（需负责人/网站控制者配合）：robots.txt 放行 GPTBot/ClaudeBot/PerplexityBot；确认关键页静态可爬（AI 爬虫不执行 JS）；llms.txt 部署（30 分钟，低成本可选）；每页 JSON-LD（Organization + FAQPage 用 geo-faq 内容） | firela.io | 依赖负责人 |
| 1.7 | **基线测量**：50 条提示词 × ChatGPT/Perplexity/Gemini/Claude 人工实测，记录"提及 FIREla / 引用 URL / 引用竞品"三列表 → 存为基线表（本规划附件模板） | 人工 ~1.5h | — |
| 1.8 | GA4 + UTM 规范落地 firela.io（`utm_source=chatgpt/perplexity/...`），为归因闭环做准备 | firela.io | 依赖负责人 |

**阶段验收**：GitHub 面全绿；Wikidata 条目上线；两个第三方列表提交；基线表 v1 完成。

### 阶段二：内容工程（9/29 – 11/10，六周）

**目标：按论文实证手段（引语 +40.9% / 统计 +30.6% / 来源标注 +27.5% / answer-first）生产与改造内容。**

| # | 动作 | 说明 |
|---|---|---|
| 2.1 | **docs.firela.io FAQ 页**：geo-faq 12 条 answer-first 化（每条标题下 100 字内直接结论），配 FAQPage JSON-LD | 内容已备，改造成本低 |
| 2.2 | **教程矩阵**（4 篇起步，对应长尾用例词）：① Alipay/WeChat 账单导入 Beancount 全流程 ② PII sanitizer 工作原理（11 类检测/29 国 IBAN 校验）③ firela-bot Cloudflare 自部署指南 ④ HSBC HK/Degiro 账单解析。每篇：answer-first 开头 + 具体数字 + 来源标注 + 带日期 | Medium + docs 双发 |
| 2.3 | **对比内容**："Beancount vs Actual Budget: mobile workflows"、"Open source YNAB alternatives"（对标策略：不攻击，陈列事实差异——开源协议/本地处理/格式开放） | Neutral facts only |
| 2.4 | **Reddit 90/10 运营启动**：r/beancount、r/plaintextaccounting 每周 1-2 次真实回答（个人号，披露开发者身份），不贴链接先立信任 | 人工，每周 ~1h |
| 2.5 | **统计与引语注入**：所有对外内容引用 fact-sheet 数字（10 解析器/11 类检测/29 国）——这正是论文里 +30.6% 的"统计手段"；引语可引用 Beancount 作者/社区 KOL 公开言论（需对方许可或为公开表述） | — |
| 2.6 | **发布纪律**：每次 GitHub Release 都写 release notes（AI 引擎引用 releases 频率高）；firela-bot 每次功能更新 = 一条产品更新帖素材 | — |

**阶段验收**：docs FAQ/教程 4+ 页上线；Medium ≥3 篇；Reddit 真实互动 ≥6 次；AI 爬虫抓取状态健康（若 firela.io 有日志）。

### 阶段三：监测与迭代（11/10 起长期）

| # | 动作 | 节奏 |
|---|---|---|
| 3.1 | **周度引用检查**：50 提示词 × 4 引擎（人工 30 分钟），按"提及/引用 URL/竞品"三列表记录，与基线对比 | 每周一 |
| 3.2 | **缺口分析**：连续 2 周未命中的提示词 → 查 AI 实际引用了谁的什么页面 → 针对性补一篇（Medium/docs/Reddit） | 每周一 |
| 3.3 | **月度归因**：GA4 AI 渠道会话（utm_source 标签）+ GitHub star 新增趋势对照 | 每月 |
| 3.4 | **飞书周报加 GEO 段**：`🔍 GEO：命中 X/50 · 新增引用 Y · 本周动作 Z`（自动化：可用 API 批量问询 4 引擎，成本 ~¥1/周，可选） | 每周一 |
| 3.5 | **上游集成探索**（Canva 模式，低优先）：firela-bot 的 MCP server 化（让 AI 助手直接查账本）——产品动作，视 bot 用户量决定 | 视需求 |

---

## 四、KPI（现实校准版）

| 指标 | 基线 | 30 天 | 90 天 |
|---|---|---|---|
| 品类词 FIREla 被提及率（15 条品类+用例词） | ≈0% | ≥20% | **≥50%**（小品类可拥有） |
| 品牌词回答准确率（事实一致） | 未测 | ≥80% | ≥95% |
| Perplexity 用例词引用 firela.io/GitHub | ≈0 | ≥1 次 | 3+ 个用例词进入答案 |
| Reddit 真实互动（条/周） | 0 | 3 | 5+ |
| 第三方权威位（Wikidata/列表站） | 0 | 2 | 3+ |
| GitHub stars（间接代理） | 18/167 | +10/+30 | M1 目标对齐 v2.0 计划 |

> 现实校准说明：附件调研的 +663%/2%→31% 来自 B2B SaaS 预算盘。FIREla 品类小 → **绝对量小但可得性强**（几乎没有竞争对手做 GEO）；"拥有品类词"比"争夺大词份额"更符合独立项目阶段。

---

## 五、与现有自动化资产的复用关系

| 现有资产 | 在 GEO 中的角色 |
|---|---|
| brand-kit 事实表/FAQ/首发内容 | 阶段二内容工程的原料（answer-first 改造底稿） |
| 内容生成器（brand-knowledge v3） | 事实一致性保障：AI 生成帖子的数据全部可回溯 fact-sheet |
| Horizon 雷达 | 竞品动态监控（Actual/Firefly/Maybe releases = 对比内容素材）+ 行业话题雷达 |
| 飞书周报 | 承载 GEO 指标段（3.4）与执行提醒 |
| 数据三层备份 | GEO 内容资产（docs/Medium 文稿）纳入备份范围 |

---

## 六、风险与现实约束

| 风险 | 应对 |
|---|---|
| firela-app 未上架，"best app" 类内容无法理直气壮 | 以 firela-bot（可用）为参战主体；app 统一 "coming soon, follow the repo"；把"诚实状态帖"本身做成信任内容 |
| 维基百科知名度门槛未达 | 不强攻；用 Wikidata（无知名度要求）+ plaintextaccounting.org/AlternativeTo 替代 |
| 独立开发者带宽 | GEO 时间盒：每周固定 2-3h（周报检查 0.5h + 内容 1.5h + 互动 0.5h）；宁少勿编 |
| 事实编造被 AI 引用 = 品牌灾难 | 已有机制：fact-sheet 唯一来源 + 生成器事实回溯 + 人工审核闸门——GEO 时代这条纪律价值翻倍 |
| firela.io 改动依赖负责人 | GitHub 面先行（完全可控）；官网改动列依赖清单集中一次过 |
| llms.txt 收益不确定 | 按调研结论：30 分钟成本部署即可，不追加投入 |

---

## 七、立即行动（本周，无需等待）

1. ✅ firela-app 最新代码拉取 + 品牌文档复检（已完成，事实零变化）
2. ▶ firela-app README 修正应用（清单在 brand-kit；fire-la 仓库需 org 权限——网页操作或给我加权限的 token）
3. ▶ GitHub org profile + Discussions + topics（0.7h，同上权限约束）
4. ▶ 50 条提示词基线表建表并做首轮测量（1.5h，我可执行，产出基线表）
5. ⏸ Wikidata / 列表站申请（注册账号后我可代办，或给步骤你操作）
6. ⏸ firela.io 技术审计与 GA4（需网站控制者配合，建议会上提出）

---

*配套：`GEO推广调研与实施方案.md`（行业调研底稿）· `brand-kit/`（内容原料）· `OPERATIONS.md`（系统运维）*
