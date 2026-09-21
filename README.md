# firela-geo

> GEO (Generative Engine Optimization) toolkit for **FIREla** — the open-source
> (AGPL-3.0) Beancount ecosystem for privacy-first personal finance.
>
> Deployables, a 50-prompt measurement baseline, strategy roadmap, and listing
> copy — everything needed to make FIREla citable by AI engines
> (ChatGPT / Perplexity / Gemini / Claude / AI Overviews).

**Status**: v0.1 (Phase 1 assets complete — see [strategy/geo-90day-roadmap.md](strategy/geo-90day-roadmap.md))
**Fact baseline**: verified against source code, as of 2026-09-16

---

## Why

AI engines now answer "best beancount mobile app" or "how to import Alipay into
Beancount" directly — with only 2-3 cited sources and ~8% click-through on AI
summaries (Pew, 2025). In our niche those answers are currently **empty or
outdated**. This repo exists to own that space with verifiable facts only:
our scoring rubric, llms.txt, JSON-LD, and tracking prompts all trace back to
the [verified fact sheet](deploy/README-deploy.md#facts).

Evidence-based tactics only (Princeton GEO study, KDD'24): citations of
sources +27.5%, statistics +30.6%, expert quotes +40.9%, fluency +28%.
Keyword stuffing measurably **hurts** (-8.3%) and is banned from our content.

## Repository layout

```
deploy/      → copy to firela.io web root (llms.txt, robots.txt, JSON-LD)
tracking/    → 50-prompt baseline CSV + Wikidata entity spec
listings/    → third-party listing applications (plaintextaccounting.org, AlternativeTo)
strategy/    → 90-day roadmap, implementation plan, industry research
tools/       → open-source monitoring setup (geo-aeo-tracker)
```

## Quick start

### 1. Deploy to firela.io (site owner, ~15 min)

- Copy `deploy/robots.txt` → web root (allows GPTBot / ClaudeBot / PerplexityBot / OAI-SearchBot…)
- Copy `deploy/llms.txt` → web root (`https://firela.io/llms.txt` must resolve)
- Inject `deploy/jsonld/organization.jsonld` into the homepage `<head>`
- Host the FAQ page with `deploy/jsonld/faq.jsonld` (FAQPage schema)
- Verify pages are static or SSR — AI crawlers do not execute JavaScript
  (Vercel: 34%+ of AI-crawler hits hit JS-only pages)

### 2. Baseline measurement (weekly, ~30 min)

- `tracking/prompt-baseline.csv` — 50 prompts across brand / category /
  use-case / comparison / 中文 queries
- Run each against ChatGPT, Perplexity, Gemini, Claude weekly; record
  `firela_mentioned / cited_url / competitor_mentioned` in the week columns
- First round = the baseline; every unfilled prompt becomes a content task

### 3. Entity & listings

- Create the Wikidata item per [tracking/wikidata-item-spec.md](tracking/wikidata-item-spec.md)
- Submit listings per [listings/third-party-listings.md](listings/third-party-listings.md)
  (plaintextaccounting.org → AlternativeTo → awesome-lists)

## Open-source stack (all overseas-friendly, see [docs/open-source-tools.md](docs/open-source-tools.md))

| Tool | License | Role |
|---|---|---|
| [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) | MIT | Local-first visibility dashboard (6 models via Bright Data) |
| [llms.txt spec](https://llmstxt.org) / [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) | n/a / MIT | Content map for AI crawlers |
| [GEO-optim/GEO](https://github.com/GEO-optim/GEO) | MIT | Princeton GEO-bench (evidence base) |
| schema.org JSON-LD | n/a | FAQPage / Organization / SoftwareApplication |

## Strategy documents

- [strategy/geo-90day-roadmap.md](strategy/geo-90day-roadmap.md) — 90-day
  three-phase plan (CN): audit & baseline → content engineering → monitoring
- [strategy/implementation-plan-2026-09.md](strategy/implementation-plan-2026-09.md) —
  this round's execution plan
- [strategy/research/](strategy/research/geo-promotion-research-2026-09-14.md) —
  industry research digest (Princeton/Pew/Semrush data, company cases, tool landscape)

## Fact discipline

Every public claim must trace to the verified fact sheet. The content
generator is grounded on the same baseline — fabricated numbers ("12
regions") were a real bug we fixed. When facts change: update the fact
sheet first, then date-stamp, then propagate.

---

## 中文说明

本仓库是 FIREla 的 GEO（生成式引擎优化）工具仓：包含 firela.io 待部署的
llms.txt / robots.txt / 结构化数据、50 条提示词基线集与测量表、Wikidata 与
第三方列表申请物料、90 天路线图与行业调研。

- 策略：不打大词，**拥有长尾品类词**（beancount mobile app / 支付宝导入
  beancount / 隐私预算追踪）——这些查询目前没有被 AI 引用过的权威答案
- 只用实证手段：来源标注 +27.5%、统计数字 +30.6%、引语 +40.9%；禁止关键词堆砌
- 事实纪律：一切数字可回溯 `deploy/README-deploy.md` 事实表

上传到 GitHub：

```bash
cd firela-geo
git remote add origin git@github.com:yuming77/firela-geo.git
git push -u origin main
```
