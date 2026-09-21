# FIREla GEO 落地实施计划（执行轮）

> 日期：2026-09-16 · 依据：《firela-geo-plan.md》90 天路线图的阶段一（基建与基线）
> 本轮原则：**只做现在就有权限做的事**——全部落地到 firela-social 仓库 `brand-kit/geo/`，firela.io 网站侧与 fire-la 组织侧产出"待部署包"，需要权限的动作明确标注

---

## 一、本轮做什么（与为什么）

| 模块 | 产出 | 状态 | 依据 |
|---|---|---|---|
| **监测基建** | 克隆开源 [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker)（257★，MIT，local-first）到本机，导入 50 条提示词集 | ✅ 完成（Bright Data key 为可选步骤，见 §4） | 调研"开源品牌监测"节 |
| **llms.txt** | `brand-kit/geo/llms.txt`（按 llmstxt.org 规范手写，比生成器更准——内容直接来自 fact-sheet） | ✅ 完成 | 调研"低成本可选基建"：30 分钟成本，不追加投入 |
| **结构化数据** | `brand-kit/geo/jsonld/`：Organization + SoftwareApplication（firela-bot）+ FAQPage（12 条问答） | ✅ 完成 | 论文实证：结构化是 GEO 核心手段 |
| **robots.txt 建议** | `brand-kit/geo/robots.txt`：放行 GPTBot/ClaudeBot/PerplexityBot/Google-Extended 等 | ✅ 完成 | AI 爬虫放行（搜索用途 UA 单独配置） |
| **50 条提示词基线集** | `brand-kit/geo/prompt-baseline.csv`（品牌 8 + 品类 15 + 用例 15 + 对比 7 + 中文 5）+ 测量记录表结构 | ✅ 完成 | 基线是一切优化的前提 |
| **Wikidata 条目规格** | `brand-kit/geo/wikidata-item-spec.md`（字段、claim、sameAs 全部备好） | ✅ 完成（创建动作需 Wikidata 账号，网页 10 分钟） | 调研"权威信源占位"：维基系占 ChatGPT 引用 47.9% |
| **第三方列表文案** | `brand-kit/geo/third-party-listings.md`：plaintextaccounting.org 工具页、AlternativeTo、awesome-beancount 的申请文案与目标路径 | ✅ 完成（公开提交前建议过目） | 细分权威背书 |
| **官网待部署包** | 以上 geo/ 文件即 firela.io 的"待部署包"——网站负责人可直接上传 robots.txt/llms.txt/JSON-LD | ✅ 交付 | AI 爬虫不执行 JS，静态文件最稳 |

**明确不做**（本轮）：firela.io 网站改动（需负责人）；fire-la 组织仓库改动（需 org 权限）；Wikidata 条目实际创建（需 Wikidata 账号）；公开第三方 PR 提交（内容代表品牌，建议你过目后提交）；付费监测工具。

---

## 二、执行顺序（本轮实际操作记录）

1. 克隆 geo-aeo-tracker → `~/workspace/geo-aeo-tracker`（本机仪表盘，Next.js）
2. `brand-kit/geo/` 七件套产出（llms.txt / robots.txt / jsonld ×3 / 提示词 CSV / Wikidata 规格 / 第三方列表文案）
3. 50 条提示词按四引擎设计（ChatGPT / Perplexity / Gemini / Claude），测量表含 8 周追踪列
4. firela-social 提交推送 + 本报告输出

---

## 三、上线动作清单（需要权限的三组，各 10-30 分钟）

### A 组：firela.io 网站负责人
- [ ] 上传 `brand-kit/geo/robots.txt` 到站点根目录
- [ ] 上传 `brand-kit/geo/llms.txt` 到站点根目录（https://firela.io/llms.txt 可访问）
- [ ] `jsonld/organization.jsonld` + `faq.jsonld`（FAQPage）注入首页与 FAQ 页 `<head>`（FAQ 页本身需先建，内容用 geo-faq.md）
- [ ] 确认关键页为静态/SSR（AI 爬虫不执行 JS）
- [ ] （可选）GA4 + AI 渠道 UTM 规范

### B 组：GitHub（fire-la org 权限，或网页操作）
- [ ] firela-app README 应用修正清单（brand-kit/firela-app-readme-fixes.md）
- [ ] fire-la org 首页 README + 双仓库 About/topics
- [ ] firela-bot 开启 Discussions

### C 组：Wikidata + 第三方列表
- [ ] 按 `wikidata-item-spec.md` 创建 FIREla 实体（网页 10 分钟）
- [ ] 按 `third-party-listings.md` 提交 plaintextaccounting.org / AlternativeTo 收录申请

### D 组：监测首测（可选，需要 Bright Data 免费账号）
- [ ] geo-aeo-tracker 本地 `npm install && npm run dev` → 设置页填 Bright Data API key → 导入 `prompt-baseline.csv` 提示词 → 跑首轮基线
- [ ] 无 key 备选：人工按 CSV 在四引擎逐条查询，结果记入 CSV 追踪列（每轮 ~40 分钟）

---

## 四、KPI 与节奏（对齐 90 天路线图）

- **基线**：首轮测量后记录 50 提示词的 FIREla 提及率（预期 ≈0%——这正是机会）
- **周节奏**：每周一按 CSV 逐条测量 30 分钟 → 未命中的提示词对照竞品页面 → 产出一条补内容任务进飞书周报
- **30 天目标**：品类词（beancount mobile app 等）提及率 ≥20%；品牌词回答准确率 ≥80%
- **90 天目标**：品类词 ≥50%；Wikidata + 两个第三方列表上线；docs FAQ 页被 Perplexity 引用 ≥1 次

---

## 五、成本

| 项 | 成本 |
|---|---|
| geo-aeo-tracker + 本地运行 | $0（MIT 开源；Bright Data 有免费试用额度）|
| llms.txt / JSON-LD / robots.txt | $0（手写，已备好）|
| Wikidata / AlternativeTo / plaintextaccounting.org | $0（账号注册即可）|
| 可选：API 化自动测量 | $5-15/天（OpenAI/Perplexity API，非必需）|
