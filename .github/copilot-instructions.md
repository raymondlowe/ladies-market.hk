# Copilot Instructions

## Research and Data Collection
- **Always use MCP servers** for research tasks
- **Handle timeouts gracefully**: If MCP servers timeout, back off for 30-60 seconds using `sleep`
- **Use GA4 and GSC data**: Always refer to analytics insights using the `ga4-gsc-mcp` server for live data, or the /.private/google-search-console-reports/ folder for historical data
- **Research thoroughly**: Use Tavily to research unknown topics. Never invent or assume information—always verify with search and extract tools
- **Prioritize keywords**: Use the KeywordsEverywhere MCP server to prioritize based on search volume and commercial value
- **Gap Analysis**: Identify content gaps by comparing with competitors and using the Tavily MCP server for insights
- **Fresh Content**: Look for topics that need updating or new content based on recent trends and user interests

## Project Management and Logging
- **Log all activities**: Write detailed logs in the `.private` folder
- **Check previous work**: When starting a job, review the `.private/last-job` file to understand what was last completed and what needs to be done next
- **Store working files**: Use the `.private` folder for research results to avoid duplicate effort

## HTML and Template Management
- **Respect editable regions**: When editing HTML pages, only make changes within "editableRegion" boundaries if they exist
- **Edit templates, not pages**: For webpages using templates with editableRegions, make changes only in the template `.dwt` file referenced in the HTML header, then replicate the changes to the individual page files if necessary
- **Use shell scripts for bulk edits**: Employ `.sh` scripts with `sed`, `awk`, `sed` etc. for bulk operations (e.g., updating copyright notices). Avoid using diffs for such tasks
- **Create pages from templates**: Always use `cp <templatename>.dwt <new-filename>.html` when creating new pages

## Quality Control and Documentation
- **Update instructions when needed**: If you make a mistake and correct it, update these instructions in the `.github/copilot-instructions.md` file. It is ok to include learnings that are specific to this project / destination
- **Document completed work**: When finishing a job, update the `.private/last-job` file with details of what was accomplished and next steps
- **Verify all changes**: Always check your work—don't assume edits or shell commands executed correctly. Review files to confirm expected changes occurred

## Additional instructions

- Do NOT add individual adsense units, rely ONLY upon the AutoAds script in the header.

- Write text in full rich prose suitable for a travel guide. Use bullet points only for things that really are a list, for other items expand a concept into one or more paragraphs. Break it up to avoid walls for text with "tips", lists or "see also", but be sure to include verbose explanatory well written prose with the vocabulary and reading level of middle school. - Instead of  `<li><strong>Clay Pot Cooking</strong>: Traditional vessels that enhance flavor development</li>` use `<p><strong>Clay Pot Cooking</strong>: These traditional vessels, crafted with care and steeped in history, offer a unique method of preparing food that elevates flavors to new heights. As the clay absorbs and radiates heat evenly, it allows ingredients to meld beautifully, creating dishes that are aromatic and deeply satisfying. Discover the magic of this time-honored technique, where every meal tells a story and every bite is a celebration of local culture.`

- Make sure newly created pages are integrated into site via relevant hyperlinks from other pages, or adding into footer or navigation for high value pages.

- If you are recommending a specific place, dish, activity then use Tavily search to research and make sure it really is available at that location, and having found it get some specifics such as company names, restaurant names, addresses, prices, opening hours etc where that place, dish, activity etc is available. Store verbatim Tavily search results into the .private folder with meaningful name for future reference.

- When starting each project make good use of research tools including Tavily search, Google Analytics 4 and Google Search Console (ga4-gsc-mcp). New research should be stored verbatim in the .private folder for future reference.

