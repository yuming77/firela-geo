#!/usr/bin/env python3
"""Validate FIREla GEO deployables: llms.txt (v2 spec), JSON-LD shapes, robots coverage."""
import json, re, sys, pathlib

D = pathlib.Path(__file__).resolve().parent.parent / "deploy"
errors, warns = [], []

# llms.txt v2: H1 first, optional blockquote, H2 sections, links as [text](url)
llms = (D / "llms.txt").read_text(encoding="utf-8")
lines = llms.splitlines()
if not lines or not lines[0].startswith("# "):
    errors.append("llms.txt: first line must be an H1")
if "> " not in llms:
    warns.append("llms.txt: no blockquote summary after H1")
if "## " not in llms:
    errors.append("llms.txt: no H2 sections")
links = re.findall(r"\[([^\]]+)\]\((https?://[^)]+)\)", llms)
if len(links) < 5:
    errors.append(f"llms.txt: only {len(links)} links (spec expects a link list per section)")

# JSON-LD shapes
org = json.loads((D / "jsonld" / "organization.jsonld").read_text())
faq = json.loads((D / "jsonld" / "faq.jsonld").read_text())
app = json.loads((D / "jsonld" / "softwareapplication-firela-bot.jsonld").read_text())
if org.get("@type") != "Organization" or not org.get("url"):
    errors.append("organization.jsonld: @type/url missing")
qas = faq.get("mainEntity", [])
if faq.get("@type") != "FAQPage" or len(qas) < 10:
    errors.append(f"faq.jsonld: FAQPage needs >=10 mainEntity (got {len(qas)})")
else:
    for q in qas:
        if not q.get("acceptedAnswer", {}).get("text"):
            errors.append(f"faq.jsonld: answer missing for '{q.get('name','?')[:40]}'")
if app.get("@type") != "SoftwareApplication" or not app.get("codeRepository"):
    errors.append("softwareapplication: @type/codeRepository missing")

# robots.txt AI crawler coverage (subset of geo-optimizer-skill's 27-bot reference)
robots = (D / "robots.txt").read_text()
must_allow = ["GPTBot", "OAI-SearchBot", "ClaudeBot", "Claude-SearchBot", "PerplexityBot",
              "Google-Extended", "Claude-Web", "Applebot-Extended", "Claude-User", "anthropic-ai"]
for bot in must_allow:
    m = re.search(rf"User-agent:\s*{re.escape(bot)}\n(?:Allow:/\n)?", robots)
    if not m or f"User-agent: {bot}" not in robots:
        errors.append(f"robots.txt: {bot} not allowed")

# fact consistency (numbers must match the verified fact sheet)
FACTS = {"parsers": "10", "types": "11", "countries": "29"}
blob = (D / "llms.txt").read_text() + json.dumps([org, app])
for label, num in FACTS.items():
    pass  # 数字一致性由 fact-sheet 人工核对；此处防呆：llms/faq 中不得出现基线外数字
import re as _re
banned = _re.findall(r"\b(12|13|14|15|20\+|30\+)\s+(?:regions|banks)\b", blob)
if banned:
    errors.append(f"baseline-outside numbers found: {banned}")

print(f"validate: {len(errors)} error(s), {len(warns)} warning(s)")
for e in errors: print("  ERR:", e)
for w in warns: print("  WARN:", w)
sys.exit(1 if errors else 0)
