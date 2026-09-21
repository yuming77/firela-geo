# GEO（生成式引擎优化）推广方案

> 调研日期：2026-09-14
> 范围：前沿科技公司 GEO 实践、开源项目生态、可落地的完整执行方案

---

## 一、背景：为什么现在必须做 GEO

GEO（Generative Engine Optimization，生成式引擎优化）由普林斯顿大学于 2023 年提出（论文 [arXiv:2311.09735](https://arxiv.org/abs/2311.09735)，KDD 2024），目标是让品牌内容在 ChatGPT、Perplexity、Google AI Overviews、Claude、Gemini 等 AI 的回答中被**引用和提及**。

关键数据支撑：

- **普林斯顿 GEO-bench**（10,000 条查询实测）：优化后内容在 AI 回答中的可见度最高提升 **40%**（Perplexity 实测 +37%）
- **Pew Research 2025.7**（68,879 次真实搜索）：出现 AI 摘要时仅 8% 用户点击任何链接（无摘要时 15%），仅 1% 点击摘要内链接 —— **"被引用"本身就是 KPI**，零点击时代已来
- **Semrush 17 个月点击流研究**：ChatGPT 引荐流量 2025 年增长 206%，但 30%+ 流向仅 10 个域名 —— 头部马太效应强，**先发优势随引用历史复利，晚入场成本更高**

### GEO 与 SEO 的本质区别

| 维度 | SEO | GEO |
|---|---|---|
| 优化目标 | 链接列表中的排名位置 | AI 回答中的内联引用 |
| 竞争格局 | 前 10 位都有流量 | 生成式回答通常只引 2–3 个来源，"AI 搜索中没有第 7 位" |
| 有效手段 | 外链、关键词 | 可验证信息密度、结构化、实体权威 |
| 失效手段 | — | 关键词堆砌实测 **-8.3%**（唯一负效手段） |

**弯道超车效应**：对 Google 排名第 5 的页面做"标注引用来源"优化，AI 可见度 +115%；排第 1 的反而 -3%。GEO 是腰部内容的超车通道。

---

## 二、知名公司案例与效果

### 1. HubSpot（B2B SaaS）
- 策略：主题集群（topic clusters：支柱页 + 数十篇子主题深度文章）构建领域权威
- 效果：营销/CRM/销售类查询大概率引用其内容，自称 AI 搜索引用份额第一的 CRM
- 来源：[HubSpot AEO 案例](https://blog.hubspot.com/marketing/hubspot-aeo-case-study)

### 2. Canva（PLG 标杆）
- 2025 年营收 $4B，LLM 引荐（ChatGPT/Claude）占总获客流量**两位数百分比**
- 通过 ChatGPT 应用深度集成实现 2600 万次对话交互，跻身 ChatGPT 引荐域名 Top 10
- 策略核心：**"上游集成"** —— 在 AI 对话内被推荐、被唤起，而非引流到官网
- 来源：[Runable 分析](https://tryrunable.com/posts/canva-hits-4b-revenue-as-llm-traffic-explodes-2025)

### 3. B2B SaaS 代理案例（行业基准参考）
- $11M ARR SaaS 90 天项目：ChatGPT 引用 +663%、Perplexity +421%、Gemini +867%、AI 归因注册 +347%、净增 ARR $612K（[CapstonAI](https://capston.ai/case-study-b2b-saas-geo/)）
- 另一案例：ChatGPT 引用率 2%→31%、对头部竞品 Share of Voice 6%→44%（[RankScope](https://rankscope.ai/blog/geo-case-studies)）
- ⚠️ 注意：代理/工具商案例为自我披露，方向可信、幅度需审慎

### 4. 中国企业案例
- 工业传感器上市公司：AI 引用率 15%→62%，CAC -52%
- 外贸 B2B 出口商：Perplexity 引用率 4%→31%，月询盘 8→53
- 3C 跨境电商：3 个月 AI 推荐率 +205%，AI 渠道订单占 31%
- 来源：[搜狐行业观察](https://m.sohu.com/a/1054552306_122953073/)

### 5. 基建层公司（工程实践公开）
- **Vercel**：[The rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler)（GPTBot 月 569M 次抓取、Claude 370M，AI 爬虫约为 Googlebot 28%；AI 爬虫不执行 JS，404 率超 34%）、[让站点可被 AI 代理阅读](https://vercel.com/kb/guide/make-your-site-readable-by-ai-agents)、[robots.dev](https://robots.dev)
- **Cloudflare**：[AI Redirects](https://blog.cloudflare.com/ai-redirects/)（301 强制规范内容）、Radar AI Insights（每爬虫状态码分布）、2025.7 起新域名默认屏蔽训练爬虫
- **Mintlify**：为数千文档站自动生成 llms.txt 并托管 MCP

---

## 三、优化手段优先级（论文实证排序）

| 手段 | 可见度提升 | 说明 |
|---|---|---|
| 添加权威引语 | **+40.9%** | 引用行业专家/权威机构原话 |
| 添加统计数据 | **+30.6%** | 具体数字、百分比、样本量 |
| 标注引用来源 | **+27.5%** | 每条论断附出处链接 |
| 流畅度优化 | +28.0% | 清晰、直接的语言 |
| 使用技术术语 | +17.6% | 建立领域专业性 |
| 关键词堆砌 | **-8.3%** | 唯一负效手段，必须避免 |

### 内容工程要点
1. **Answer-first 结构**：标题下直接给结论，再展开论证
2. **结构化**：FAQ、对比表格、编号列表、带日期更新
3. **Schema 结构化数据**：FAQPage / Organization / HowTo / Article JSON-LD，加 Wikidata sameAs 实体消歧
4. **llms.txt**：站点根目录 Markdown 内容地图（[llmstxt.org](https://llmstxt.org)）。采用者含 Anthropic、Cloudflare、Stripe、Vercel、Supabase、NVIDIA；但采用率仅约 5.9%、主流 LLM 未承诺读取 —— 视为**低成本可选基建**，非核心策略
5. **AI 爬虫放行**：robots.txt 允许 GPTBot、ClaudeBot、PerplexityBot；用 IndexNow 加速收录
6. **JS 渲染问题**：AI 爬虫不执行 JS（Vercel 数据 404 率 34%+）—— 关键内容必须 SSR/静态化

### 权威第三方信源占位（"引用即新外链"）
AI 引擎高度依赖这些源，应主动运营：
- **维基百科**：占 ChatGPT top-10 引用的 47.9% —— 建品牌词条 + Wikidata 实体
- **Reddit**：占 Perplexity 引用的 46.5%，被引率 3 个月内从 1.3% 飙至 7.15% —— 真实用户讨论
- **YouTube**：Google AI Overviews 第一被引源
- **G2 / 评测站 / 媒体报道**：B2B 决策链的 AI 信源

---

## 四、开源项目生态（2026-09 实测 star 数）

### 核心 GEO/AEO 工具

| 项目 | Stars | 用途 |
|---|---|---|
| [yaojingang/GEOFlow](https://github.com/yaojingang/GEOFlow) | 3,627 | GEO 内容工程与多站点分发平台，AI 质检（中文社区，star 最高） |
| [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) | 2,610 | llms.txt 规范官方仓库（Jeremy Howard） |
| [onvoyage-ai/gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) | 1,303 | Claude Code Skill，站点 AEO/GEO 改进 |
| [langchain-ai/mcpdoc](https://github.com/langchain-ai/mcpdoc) | 1,033 | 将 llms.txt 暴露给 IDE/编码代理 |
| [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) | 794 | 审计工具：robots.txt、llms.txt、JSON-LD，8 大类 47 项打分（CLI+MCP） |
| [yaojingang/GEORank](https://github.com/yaojingang/GEORank) | 463 | 开源 GEO 排名与监测平台 |
| [GEO-optim/GEO](https://github.com/GEO-optim/GEO) | 330 | 原始普林斯顿论文代码 + GEO-bench 基准 |
| [elmohq/elmo](https://github.com/elmohq/elmo) | 326 | 开源 AEO/GEO 平台，追踪 ChatGPT/Claude/Perplexity/Gemini 引用 |
| [danishashko/geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) | 257 | local-first 仪表盘，6 模型提及/引用/份额追踪 |
| [firecrawl/llmstxt-generator](https://github.com/firecrawl/llmstxt-generator) | 536 | 爬任意网站生成 llms.txt / llms-full.txt |
| [cxcscmu/AutoGEO](https://github.com/cxcscmu/AutoGEO) | 215 | ICLR'26，自动学习生成引擎偏好并改写内容 |

### llms.txt 生成（按建站框架）
- **Mintlify**：内建自动生成（含免费版）+ MCP 托管
- **Docusaurus**：[@signalwire/docusaurus-plugin-llms-txt](https://github.com/signalwire/docusaurus-plugins)
- **Astro**：[4hse/astro-llms-txt](https://github.com/4hse/astro-llms-txt)
- **Sphinx**：[jdillard/sphinx-llms-txt](https://github.com/sphinx-llms-txt)
- 2026.5 起 Google Lighthouse Agentic Browsing 审计已加入 llms.txt 检查

### AI 爬虫识别与日志分析
- [@geosuite/ai-crawler-bots](https://www.npmjs.com/package/@geosuite/ai-crawler-bots)：20+ AI 爬虫 UA 库，零依赖 CLI + GitHub Action（robots.txt 审计、日志解析、CI 门禁）
- Nginx：`map $http_user_agent` 将 GPTBot/ClaudeBot/PerplexityBot 分类聚合
- 注意 Claude-Web/Claude-SearchBot（搜索用途）与 ClaudeBot（训练用途）UA 不同

### 开源品牌监测（自建替代商业工具）
- 最可用起点：[elmo](https://github.com/elmohq/elmo)（326★）、[geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker)（257★，四指标：mention/position/share-of-voice/citations）
- AWS 参考架构：[aws-samples 引用分析](https://github.com/aws-samples/sample-llm-search-citation-analysis-with-amazon-bedrock)（22★，Step Functions + React 全套）
- DIY 成本：约 $5–15/天跑 100 条 prompt（用 OpenAI/Perplexity/Gemini API，教程见 [DEV](https://dev.to/benedictmendoza/how-to-track-your-brands-visibility-in-chatgpt-perplexity-gemini-geo-monitoring-with-code-5701)、[Apify](https://blog.apify.com/measure-llm-brand-visibility/)）

### 商业监测工具对比

| 工具 | 起价 | 定位 |
|---|---|---|
| [Profound](https://www.tryprofound.com) | $499/月 | 企业级，19 亿真实用户提示词，8 引擎，转化归因 + API |
| [Peec AI](https://peec.ai) | €89/月 | 中端，每日追踪、竞品差距分析 |
| [Otterly.ai](https://www.amicited.com/reviews/best-otterly-ai-alternatives/) | $29/月 | 中小企业，GEO 建议 + 内容简报 |

---

## 五、执行方案（90 天三阶段）

### 阶段一：诊断与基建（第 1–2 周）

**目标：可被抓取、可被解析、可被测量**

1. **技术审计**（用 [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) 或 [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) Claude Code Skill 跑 47 项审计）：
   - robots.txt 放行 GPTBot / ClaudeBot / Claude-Web / Claude-SearchBot / PerplexityBot / Google-Extended（按需）
   - 关键页面 SSR/静态化（AI 爬虫不执行 JS）
   - 修复高 404 率页面（Vercel 数据：AI 爬虫 404 率 34%）
2. **结构化数据**：全站加 Organization + Article + FAQPage JSON-LD，Wikidata sameAs 实体消歧
3. **部署 llms.txt**：用 [firecrawl/llmstxt-generator](https://github.com/firecrawl/llmstxt-generator) 或框架插件生成，30 分钟成本，收益不确定但无风险
4. **建立基线**：部署 [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker)（或 elmo）+ GA4 AI 渠道归因，定义 50–100 条核心提示词集（品牌词 + 品类词 + 竞品对比词），记录当前 AI Share of Voice 基线

### 阶段二：内容工程（第 3–8 周）

**目标：按论文实证的最优手段重写/新建内容**

1. **Answer-first 改造**Top 20 核心页面：
   - 每页标题下 100 字内直接给结论
   - 注入统计数据（+30.6%）、权威引语（+40.9%）、每条论断标来源（+27.5%）
   - 删除关键词堆砌（-8.3%）
   - 加 FAQ 区块、对比表格、带更新日期
2. **主题集群建设**（HubSpot 模式）：1 个支柱页 + 10–20 篇子主题深度文章，构建领域权威信号
3. **权威信源占位**：
   - 维基百科词条（若达到收录标准）+ Wikidata 实体
   - Reddit 真实运营（AMA、回答相关 subreddit 提问）
   - G2/Capterra 评测、行业媒体投放
4. **上游集成探索**（Canva 模式）：评估 ChatGPT app / MCP server / 插件形态，让产品在 AI 对话内被直接唤起

### 阶段三：监测与迭代（第 9–12 周，及长期）

1. **每日追踪**：AI 引用率、Share of Voice、品牌提及与情感、AI 引荐会话与转化
2. **周迭代**：对未引用的提示词，分析 AI 实际引用了哪些竞品页面 → 针对性补内容
3. **月复盘**：AI 归因注册/询盘（GA4 UTM：`utm_source=chatgpt / perplexity / gemini`）
4. **日志侧监控**：Nginx/Cloudflare/Vercel bot 分析，确认 AI 爬虫抓取频率与状态码健康

### KPI 与预期（参考行业基准）

| 指标 | 基线 | 90 天目标 |
|---|---|---|
| 核心提示词被引用率 | 测量得出 | +2–3 倍（案例区间：2%→31%） |
| Share of Voice（vs 头部竞品） | 测量得出 | 6%→40% 区间可期 |
| AI 归因转化 | 0 或未测量 | 建立归因闭环 |

---

## 六、风险与注意事项

1. **代理案例数据（+663% 等）为自我披露**，方向可信、幅度打折看；独立数据（普林斯顿、Pew、Semrush）锚定真实上限约 40%
2. **llms.txt 争议大**：Google John Mueller 公开拒绝（类比废弃的 keywords meta tag），主流 LLM 未承诺读取 —— 不要投入超过半小时
3. **头部马太效应**：ChatGPT 引荐流量 30% 流向 10 个域名，越早入场复利越强
4. **AI 爬虫与成本**：放行 AI 爬虫会增加带宽成本（Cloudflare 2025.7 起默认屏蔽训练爬虫），需权衡训练用途 vs 搜索用途的 UA 分别配置
5. **工具均为诊断型**：Profound 等定位可见性缺口后，内容生产与权威建设仍需自建执行

---

## 附：核心来源

- 普林斯顿 GEO 论文：https://arxiv.org/abs/2311.09735 （代码：https://github.com/GEO-optim/GEO）
- Pew Research AI 摘要点击研究（2025.7）
- Semrush ChatGPT 引荐流量研究：https://www.semrush.com/blog/chatgpt-search-insights/
- Vercel AI 爬虫报告：https://vercel.com/blog/the-rise-of-the-ai-crawler
- llms.txt 规范：https://llmstxt.org
- GEO 论文持续追踪：https://github.com/Wu-beining/generative-engine-optimization-research-hub
