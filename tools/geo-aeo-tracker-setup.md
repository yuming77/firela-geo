# geo-aeo-tracker setup (FIREla notes)

Local clone: `~/workspace/geo-aeo-tracker` (MIT, local-first Next.js dashboard).

## Run locally (no cloud needed)

```bash
cd ~/workspace/geo-aeo-tracker
npm install
npm run dev        # http://localhost:3000
```

Live AI checks require a **Bright Data** account + AI Scraper API key
(free trial credits available). Paste the key in the dashboard settings.

## Import the FIREla prompt set

`tracking/prompts.ts` in this repo contains the 50 FIREla prompts as a
`TaggedPrompt[]` array (`{ text, tags }`) matching the tracker's demo format —
paste it into the tracker's prompt config (replace the demo `PROMPTS` array).
The source of truth is `tracking/prompt-baseline.csv` (50 rows, tag + category
columns included).

## Weekly measurement routine (~30 min)

1. Open the dashboard → run the 50 prompts across ChatGPT / Perplexity /
   Gemini / Claude (manual query or Bright Data-backed run).
2. For each prompt record: FIREla mentioned? cited URL? competitor mentioned?
3. Fill the week columns in `tracking/prompt-baseline.csv` (w1…w8).
4. Any prompt with no FIREla mention for 2 consecutive weeks → create a
   content task (docs page / Medium post / Reddit answer) targeting it.

## Upgrade path

- Outgrow manual tracking → wire the Bright Data API into a scheduled job,
  or evaluate `elmohq/elmo` as a hosted dashboard.
