
# WLMedia Unified Style Guide

## Purpose
Accelerate consistent, high-quality improvements to travel/local-attraction microsites—maximizing content clarity, SEO, monetization, accessibility, and technical hygiene—while avoiding low-value churn.

---

## 1. Content Structure & Readability
- Break up “walls of text” with callout boxes, tips, lists, and colored backgrounds.
- Use scannable sections, clear headings, and visual breaks for easier reading.
- Always introduce a page with a concise, value-focused summary.
- Expand stub pages with more interesting related material, a stub page is one with less than 100 words of conten. Do not have sparse content, always expand into detailed, engaging guides.
- Prefer active voice and concrete specifics over generic filler.


## 2. Outgoing Links & Verification
- Every real-world object (restaurant, club, attraction, service) must have a real, authoritative external link.
- Use Tavily search to find links and Tavily extract to confirm they work and are relevant.
- Remove or fix broken links; substitute with review sites or official pages if needed.
- All external links must use `target="_blank"`.
- When mentioning services (e.g., “luxury airport transfers”), link to a reputable provider.

## 3. Internal Linking & Cross-Linking
- Add comprehensive cross-linking between related guides and pages.
- Interlink our own sites where appropriate to deepen topical relevance and conversion.
- Ensure new/expanded pages are integrated via navigation, footer, or relevant hyperlinks.

## 4. SEO & Keyword Strategy
- Use Keywordseverywhere MCP server to prioritize high-value keywords (search volume, CPC).
- Use Keywordseverywhere PASF (People Also Search For) to branch out into related topics.
- Each page must have a unique, natural-language H1 containing the primary intent phrase.
- Add 1–2 internal links to other relevant site pages using descriptive anchor text.
- Where natural, link out once to a reputable authoritative external source.
- Ensure meta description is 140–155 chars, compelling, and benefit-driven.

## 5. Monetization & Performance Analysis
- Use ga4-gsc-mcp server to check actual performance (impressions, clicks, income) per site and per URL.
- Seek opportunities: prioritize pages ranking worse than page 1 but with high impressions or high CPC value.
- Remove hard-coded AdSense units; ensure only AutoAds is used.
- Preserve ad placeholders unless they block readability or accessibility.
- Improve content density around ad slots with genuine informational value.

## 6. Technical Hygiene & Accessibility
- Fix navigation errors (e.g., case-sensitive filenames causing 404s).
- Repair broken styling and ensure template consistency.
- Use bulk tools (sed, scripts) for repetitive fixes.
- Every <img> requires meaningful alt text.
- Heading sequence must be logical; link text must describe destination purpose.
- Use mobile-responsive design for new UI elements.

## 7. Value & Authority
- Add authentic business links (official, TripAdvisor, Facebook, etc.).
- Prefer concrete, actionable details over generic filler.
- Identify at least one differentiator per page (local nuance, timing, insider navigation, seasonal caveat).
- Consider the current date (`date`) and mention upcoming or seasonal topical items for 2025 and 2026 to show real involvement with the location.

## 8. Research & Expansion
- When you find one object at a location, research to find similar or additional (e.g., more beaches, restaurants, dishes, entrance fees).
- Consider pain points for the potential visitor (clues in the "People Also Search For") and address those pain points with actionable grounded truths, researching first to be sure and linking to outside resources as evidene.
- Store verbatim Tavily search results in the .private folder with a meaningful name for future reference.
- Research by checking already saved search and resresaerch aerch material in .private but then extending with Tavily searches and extracting relevant content.
- Use Youtube transcripts and Tavily extract for real user experience tips and recommendations.

## 9. Git & Issue Workflow
- Each change should map to an issue; reference it in commit messages (#ISSUE_NUMBER).
- Use small, cohesive commits (content restructuring vs. media alt fixes vs. internal links).
- No force pushes; branch naming: feature/<short-topic> or content/<page-slug>.
- Never commit secrets or large binaries (>5MB) without approval.

## 10. Definition of Done (DoD)
A page refactor is complete only when:
- Structure: Sections are logically chunked; heading hierarchy valid.
- Readability: No paragraph > ~250 words; clear intro + optional concise conclusion.
- SEO: Unique H1; internal link(s) added if appropriate; no keyword stuffing.
- Accessibility: Alt text passes quick check; headings and lists semantic.
- Value: At least one unique contextual insight added.
- Callouts: Only high-value; properly formatted.
- Clean HTML: No stray inline styles, dead comments, or duplicated includes.
- Links: Checked for obvious typos and confirmed with Tavily extract.
- Commit(s): Reference issue, descriptive message.

## 11. Anti-Patterns (Avoid)
- Creating artificial subheadings every 1–2 sentences just to add headings.
- Repeating the primary keyword unnaturally.
- Adding trivial callouts (“Bring cash” if already obvious/repeated).
- Copying generic travel boilerplate from other pages.
- Inflating word count without substantive information.
- Introducing technology or layout rewrites absent an explicit modernization issue.

## 12. Tone & Style
- Informative, neutral-positive, pragmatic; no hypey marketing tone.
- Use second person sparingly; prefer objective guidance.
- Prefer present tense for enduring facts; specify temporal qualifiers for seasonal or time-bound details.

## 13. Quick Editing Heuristic
If a paragraph offers: who / what / why / when / how (actionable detail) → keep/refine.
If it repeats context already stated without new actionable insight → compress or remove.

---

## MCP Server Usage Summary
- **Tavily Search & Extract**: Always use for outgoing link research and verification.
- **Keywordseverywhere**: Prioritize high-value keywords, expand into related topics, and identify new content opportunities.
- **ga4-gsc-mcp**: Analyze actual performance, find high-opportunity pages, and guide interlinking and expansion.

---

## Rollout Strategy
1. Each repo’s .github/copilot-instructions.md should begin with:
   ```
   [GLOBAL STYLE GUIDE]
   Refer to centralized STYLE_GUIDE.md in .private for global standards. Repo file only houses repo-specific deviations.
   ```
2. For new repos, create .github/copilot-instructions.md with the above pointer and a section for local notes.
3. Use automation to sync the pointer block and monitor for drift.

---

## Example Issue Patterns
- “Break up walls of text with call outs, lists, tips, etc, needs relevant outgoing links.”
- “Fix navigation 404 errors, broken page styling, and add external links.”
- “Remove hard coded AdSense units and ensure AutoAds is used.”
- “Expand history page into a comprehensive tourist guide.”
- “Add authentic business links for venues mentioned.”
- “Cross-link related guides and integrate new pages into navigation.”

---

## Change Log
- 2025-08-13: Added MCP server usage, link verification, keyword prioritization, and interlinking policies.
