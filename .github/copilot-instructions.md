# Copilot Instructions 

## 0. Core Principles
Accuracy (verify, never assume) • Completeness (finish and log) • Reusability (store research) • Currency (always note current year: run `date`).

## 1. Quick Workflow
1. Read `.private/last-job.md` + CHANGELOG.md.
2. Open / create `.private/TODO.md`; add next actions; remove lines when done (do not just strike through).
3. Research (Tavily, Keywordseverywhere, GA4/GSC). Reuse prior material in `.private/` before new searches.
4. Implement (template first → content → links → verification).
5. Log outcome: update `last-job.md`, append CHANGELOG entry, archive prior `last-job.md` as `completed-job-YYYYMMDD-HHMM.md`.

## 2. File & Naming
`research-topic-YYYYMMDD.md`, `completed-job-YYYYMMDD-HHMM.md`. Reference issue numbers or dates in commits. Never delete raw research—append.

## 3. Error / Block Logging
Log errors or blocked tasks to `.private/errors.md` with timestamp + cause + proposed next step.

## 4. Research Rules
– Use MCP servers for research when saved research documents in .private are inadaquate (Tavily, ga4-gsc-mcp, Keywordseverywhere).  
– On timeout: `sleep 30` then retry (max 3).  
– Store verbatim search/extract outputs under `.private/` with descriptive filenames.  
– Before adding a recommendation (place / dish / activity) confirm existence + specifics (name, address, hours, price) via Tavily Extract; save evidence.

## 5. Content Creation & Expansion
Stub page = <100 words of actual content (exclude template boilerplate). Create via `cp template.dwt new-page.html` immediately when a viable topic is identified; seed with verified basics. Expand pages <500 words (net content) after research; measure with `wc` minus template baseline. Always add at least one unique local nuance / tip supported by research or quotes from real user reviews.

## 6. Writing Style
Travel guide prose: clear, factual, moderately rich. Avoid bullets in prose unless for actual lists. Convert shallow bullets into explanatory paragraphs.  
Example (bad → good):  
Bad: `<li><strong>Clay Pot Cooking</strong>: Traditional vessels that enhance flavor development</li>`  
Good: `<p><strong>Clay Pot Cooking</strong>: Even heat retention lets ingredients meld, producing deeper aromas and textures; this method reflects long-rooted local cooking practice.</p>`

Keep paragraphs ≤ ~250 words; break walls of text with meaningful tips or callouts (avoid filler), use borders and colours and emoji to lightening things up. Avoid keyword stuffing. Tone: neutral-positive, authoritative, non-hype, helpful, on the reader's side.

## 7. Localization
English base; include local terms (e.g. MTR, RER, S‑Bahn) and optionally native script in parentheses. Use correct local currency symbol (HK$, €, £, US$ if non‑local source ambiguity). Provide simple pronunciation when helpful.

## 8. Linking Policy
External: each real-world entity gets one authoritative link; verify with Tavily Extract; broken → replace or remove. All external anchors: `target="_blank"`. If no official site, use reputable review / reference (Tripadvisor, Wikipedia, govt authority). Internal: ensure every new or expanded page is discoverable (contextual links + footer or nav if high value). Add 1–2 relevant internal links from the new page outward and from existing pages inward where logical.

## 9. Templates & HTML Hygiene
Edit inside editableRegion only. For structural changes edit the `.dwt`; replicate if needed. Use scripts (`sed`, `awk`) for bulk repetitive edits. Always close tags, especially `<script>`. Every `<img>` has concise descriptive `alt`. Maintain logical heading order. Remove dead comments / duplicate includes.

## 10. SEO & Keywords
Primary intent phrase appears once in natural H1. Use Keywordseverywhere (volume, CPC) + PASF for related expansions. Meta description: 140–155 chars, benefit-driven, no stuffing. Add unique insight rather than padding.

## 11. Performance & Monetization
Use ga4-gsc-mcp to spot: high impressions + low CTR/rank, high CPC terms lacking depth, pages just off page 1. Focus expansion there. Only AutoAds (no manual AdSense units). Do not degrade readability to force density around ads.

## 12. Research Expansion Heuristic
Found one beach? Look for 2–3 more notable ones. One local dish? Add other signature dishes. One fee? Gather comparable fees (hours / pricing tiers). Always cite sources in saved research files.

## 13. YouTube / First-Hand Signals
Check `.private/` for existing transcripts. If absent, use Tavily to locate relevant videos; extract transcript; save. Distill actionable visitor tips (best time, crowd patterns, hidden photo spot) and integrate succinctly. Try also tavily search for video transcripts.

## 14. Git & Issues
Every change ties to an issue (`#123`). Branch names: `content/<slug>` or `feature/<topic>`. Cohesive commits (e.g. "add external links", "expand history section"). No force push. No secrets / large binaries (>5MB). Reference issue in commit message.

## 15. Logging & Completion
When a job ends: archive old `last-job.md`, write new one (summary, what changed, next 3 priorities). Update CHANGELOG with concise bullet referencing issue.

## 16. Definition of Done (Page)
Structure logical; H1 unique. Paragraphs sized reasonably. Required internal + external verified links present. Alt text complete. At least one differentiated local context element. No unverified claims. Template integrity preserved. Commit references issue and logs added.

## 17. Anti‑Patterns (Reject)
Filler expansions; repetitive keyword stuffing; artificial micro-headings; orphan pages with no inbound links; generic travel boilerplate; adding layout rewrites without a specific modernization task; trivial callouts (e.g. obvious cash advice repeated).

## 18. Quick Edit Test
Keep only sentences adding who / what / why / when / how or unique context. Remove repetition, vague hype, or unverifiable speculation.

## 19. MCP Server Summary
Tavily Search/Extract → verify facts & links.  
Keywordseverywhere → primary + related queries (volume/CPC).  
ga4-gsc-mcp → performance triage & opportunity targeting.


## 21. Example Issue Titles
– Expand <page> to exceed 500 words with verified specifics (#123).  
– Add authoritative outbound links & fix broken anchors (#124).  
– Remove manual AdSense units; enforce AutoAds only (#125).  
– Cross-link new attraction pages in navigation (#126).  
– Fix 404s from case-mismatched filenames (#127).

## 22. Example Bullet → Paragraph Conversion (Another Sample)
Bad: `<li><strong>Beauty Services:</strong> Professional makeup application...</li>`  
Good: `<p><strong>Beauty Services</strong>: Skilled artists tailor makeup and skincare advice to visitor needs—day touring, evening dining, or photos—adding practical routines and locally relevant product guidance.</p>`

## 23. Currency & Date Awareness
Confirm year-sensitive facts (events, seasonal closures) against current year (run `date`) and adjust wording (e.g. "In 2025 the..." if time-bounded).

## 24. Ads & Monetization Guardrail
Never insert individual AdSense units. If found, remove and document in CHANGELOG + issue.

## 25. Minimal Commit Message Format
`<scope>: <action> (#issue) — <short outcome>`  
Example: `content: expand night-market guide (#342) — +750w, links verified`.

## 26. Be thorougher, use checklists.
- Make your own internal check list of tasks to do, such as pages to process, and make sure you complete them.