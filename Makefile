# FIREla GEO workflow — validate → audit → prompts → track
SHELL := /bin/bash
TRACKER_DIR ?= $(HOME)/workspace/geo-aeo-tracker

.PHONY: validate audit prompts track baseline all help

help: ## show targets
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | awk -F':|##' '{printf "  \033[36m%-10s\033[0m %s\n", $$1, $$3}'

validate: ## validate deployables (llms.txt v2 spec + JSON-LD shapes + robots coverage + fact guard)
	python3 scripts/validate.py

audit: ## run geo-optimizer-skill audit against live firela.io (needs: uv tool install geo-optimizer-skill)
	mkdir -p audits
	uv run --from $(HOME)/workspace/geo-optimizer-skill geo audit --url https://firela.io --format markdown > audits/$(shell date +%F)-firela-io.md
	@echo "saved audits/$(shell date +%F)-firela-io.md"

prompts: ## regenerate tracking/prompts.ts from prompt-baseline.csv
	python3 scripts/gen_tracker_prompts.py

track: ## run geo-aeo-tracker locally (manual measurement UI)
	cd $(TRACKER_DIR) && npm run dev

baseline: ## first-round measurement reminder (manual, 4 engines × 50 prompts)
	@echo "Open tracking/prompt-baseline.csv → query each prompt on ChatGPT/Perplexity/Gemini/Claude"
	@echo "Record: firela_mentioned / cited_url / competitor_mentioned for week 1. Then commit the CSV."

all: validate audit
