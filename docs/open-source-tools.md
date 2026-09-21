# Open-source tools used / referenced by the FIREla GEO program

> List per team request. "Overseas usable" = usable when FIREla's promotion
> targets international audiences (all tools are global, MIT/OSI-licensed or
> specification documents; none are region-locked).

## Actively used in this repo / workflow

| Project | License | Stars | Role | Overseas usable |
|---|---|---|---|---|
| [danishashko/geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) | MIT | 257 | Local-first AI visibility dashboard; tracks mention / position / share-of-voice / citations across 6 models. Cloned to `~/workspace/geo-aeo-tracker`, deps installed. Needs a free Bright Data account + API key to run live checks. | ✅ (Bright Data is a global service) |
| [llmstxt.org specification](https://llmstxt.org) ([AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt), MIT, 2,610★) | — | — | Format for `deploy/llms.txt` (hand-written from the verified fact sheet; more accurate than generators for our small site). | ✅ |
| [GEO-optim/GEO](https://github.com/GEO-optim/GEO) (Princeton GEO-bench) | MIT | 330 | Evidence base for tactic prioritization (citations +27.5%, statistics +30.6%, quotes +40.9%, keyword stuffing −8.3%). | ✅ |

## Referenced as optional / planned

| Project | License | Stars | Planned role | Overseas usable |
|---|---|---|---|---|
| [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) | — | 794 | 47-point site audit (robots / llms.txt / JSON-LD) for firela.io + docs | ✅ (Claude Code skill) |
| [firecrawl/llmstxt-generator](https://github.com/firecrawl/llmstxt-generator) | — | 536 | Alternative llms.txt generator (we hand-wrote instead — more accurate for our small site) | ✅ |
| [langchain-ai/mcpdoc](https://github.com/langchain-ai/mcpdoc) | — | 1,033 | Expose llms.txt to IDE / AI agents | ✅ |
| [elmohq/elmo](https://github.com/elmohq/elmo) | — | 326 | Open-source AEO/GEO platform (ChatGPT/Claude/Perplexity/Gemini citation tracking) — upgrade path over manual tracking | ✅ |
| [cxcscmu/AutoGEO](https://github.com/cxcscmu/AutoGEO) | — | 215 | ICLR'26 research: auto-learn generator preferences and rewrite content | ✅ (research) |
| [yaojingang/GEOFlow](https://github.com/yaojingang/GEOFlow) | — | 3,627 | CN-community GEO content platform — optional reference only (our push is international) | ✅ but CN-centric |
| [yaojingang/GEORank](https://github.com/yaojingang/GEORank) | — | 463 | GEO ranking/monitoring — alternative to geo-aeo-tracker | ✅ |
| [@geosuite/ai-crawler-bots](https://www.npmjs.com/package/@geosuite/ai-crawler-bots) | — | npm | AI crawler UA library + robots.txt audit CLI (20+ bots) | ✅ |

## Commercial tools evaluated, not used (zero-budget constraint)

| Tool | Price | Note |
|---|---|---|
| Profound | $499/mo | Enterprise share-of-voice tracking |
| Peec AI | €89/mo | Mid-market daily tracking |
| Otterly.ai | $29/mo | SMB GEO suggestions |

DIY alternative in place: manual weekly measurement of the 50-prompt set
(free), with geo-aeo-tracker / elmo as the open-source upgrade path.

## Region notes

- All tools above are globally hosted services or local-first software —
  no region locks affect international use.
- The only region-sensitive part of our stack is *content sourcing*:
  Reddit returns 403/429 to GitHub Actions / datacenter IPs (seen in
  Horizon runs) — Reddit collection stays on the home-IP collector, which
  works fine. This is a sourcing constraint, not a tool constraint.
