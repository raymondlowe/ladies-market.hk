[GLOBAL STYLE GUIDE]
Refer to centralized STYLE_GUIDE.md in .private for global standards. Repo file only houses repo-specific deviations.

# Copilot Instructions

## General Principles

- **Accuracy**: Always verify facts and edits. Never assume—always check.
- **Completeness**: Ensure all steps are finished and documented. Don’t leave tasks half-done.

## File Naming and Versioning

- Use clear, descriptive names for new files and logs (e.g., `research-topic-YYYYMMDD.md`).
- Reference job numbers or dates in commit messages and CHANGELOG entries.

## Error Handling

- Log any errors or unexpected results in `.private/errors.md` with date/time and details.
- If a task cannot be completed, document the reason and next steps.


## Date/Time awarness

Use `date` command to check the current date, pay attention to the current year.

## Research and Data Collection
- **Always use MCP servers** for research tasks
- **Handle timeouts gracefully**: If MCP servers timeout, back off for 30-60 seconds using `sleep`
- **Use GA4 and GSC data**: Always refer to analytics insights using the `ga4-gsc-mcp` server for live data, or the /.private/google-search-console-reports/ folder for historical data
- **Research thoroughly**: Use Tavily to research unknown topics. Never invent or assume information—always verify with search and extract tools
- **Prioritize keywords**: Use the KeywordsEverywhere MCP server to prioritize based on search volume and commercial value
- **Gap Analysis**: Identify content gaps by comparing with competitors and using the Tavily MCP server for insights
- **Fresh Content**: Look for topics that need updating or new content based on recent trends and user interests
- **Make stub page immediately**: When a new topic has been identified make the stub page from the template (``cp <template name>.dwt <new-page-name>.html`) immediately and populate with whatever basic information you already have on the subject, e.g. from research and searches.

## Project Management and Logging
- **Log all activities**: Write detailed logs in the `.private` folder, use the CHANGELOG.md for summaries
- **Check previous work**: When starting a job, review the `.private/last-job.md` file and the CHANGELOG.md to understand what was last completed and what needs to be done next
- **Store working files**: Use the `.private` folder for research results to avoid duplicate effort, don't cleanup, just keep everything
- **Use TODO.md**: Create, read and update a file `.private/TODO.md` with checklists of things to do. Delete items when done (don't just x mark them, actually delete them from the TODO.md file). When creating `Next steps` , `Next Priority Actions`, `Next Phase Priorities` or any thing about what is to do next append it to the TODO.md file.
- **Mark completed items DONE**: Whenever following instructions in a plan document, once a step has been completed edit the file to add DONE against the completed item with a date/time. If it is in the `TODO.md` then also delete the task line from the file.

## HTML and Template Management
- **Respect editable regions**: When editing HTML pages, only make changes within "editableRegion" boundaries if they exist
- **Edit templates, not pages**: For webpages using templates with editableRegions, make changes only in the template `.dwt` file referenced in the HTML header, then replicate the changes to the individual page files if necessary
- **Use shell scripts for bulk edits**: Employ `.sh` scripts with `sed`, `awk`, `sed` etc. for bulk operations (e.g., updating copyright notices). Avoid using diffs for such tasks
- **Create pages from templates**: Always use `cp <templatename>.dwt <new-filename>.html` when creating new pages

- **Close all tags**: Make sure that tags are closed properly, particularly `<script>` tags which must always be closed with `</script>`

## Quality Control and Documentation
- **Update instructions when needed**: If you make a mistake and correct it, update these instructions in the `.github/copilot-instructions.md` file. It is ok to include learnings that are specific to this project / destination
- **Document completed work**: When finishing a job, save the previous last-job.md file by renaming it with the file date-time to `completed-job-date-time.md`, then update the `.private/last-job.md` file with details of what was accomplished and next steps. Add a summary to CHANGELOG.md, creating it if necessary.
- **Verify all changes**: Always check your work—don't assume edits or shell commands executed correctly. Review files to confirm expected changes occurred

## Expanding the website 

- **Additional topics**: Identify topics that are missing from the website, or that could be expanded with more information, by using KeywordsEverywhere "People Also Search For" PASF to find searches that relate to the top topics mentioned in the `.private/google-search-console-reports/<domain>-query.csv`. Make stub pages from the .dwt template using `cp` and fill in with basic information from existing research first before going on to expand into indepth resource page.
- **Expand short pages**: If pages have less than 500 words then research the topic and expand it to more than 500 words. Use `wc` to count words, but compare against the 'words' of the empty template .dwt file to make sure you are counting content words, not the template boilerplate.

## Linking policy
- **Link to authoritative sources**: Use tavily search to find correct links for hotels, restaurants, shops etc and link to them.
- **Check existing and new links are valid**: Use tavily extract to load links and make sure they really are the correct thing, if they are not search again and fix the links. If no specific link is found a generic link such as Wikipedia or Tripadvisor can be substituted.
- **External links to open in new window**: All external links should use `target="_blank"` to open in a new window.

## Additional instructions

- Do NOT add individual adsense units, rely ONLY upon the AutoAds script in the header.

- Write text in full rich prose suitable for a travel guide. Use bullet points only for things that really are a list, for other items expand a concept into one or more paragraphs. Break it up to avoid walls for text with "tips", lists or "see also", but be sure to include verbose explanatory well written prose with the vocabulary and reading level of middle school. - Instead of  `<li><strong>Clay Pot Cooking</strong>: Traditional vessels that enhance flavor development</li>` use `<p><strong>Clay Pot Cooking</strong>: These traditional vessels, crafted with care and steeped in history, offer a unique method of preparing food that elevates flavors to new heights. As the clay absorbs and radiates heat evenly, it allows ingredients to meld beautifully, creating dishes that are aromatic and deeply satisfying. Discover the magic of this time-honored technique, where every meal tells a story and every bite is a celebration of local culture.` . Expand bullets into full paragraphs: instead of <li><strong>Beauty Services:</strong> Professional makeup application, skincare consultations, and color matching services</li> write <p>Travelers seeking to enhance their natural beauty or prepare for a special evening can take advantage of professional beauty services that offer a refined and personalized touch. Skilled makeup artists provide expert makeup application, adapting techniques and styles to suit each guest’s preferences—whether it’s a sophisticated look for a night out, a fresh-faced glow for sightseeing, or elegant touches for a memorable photo session. Complementing the makeup experience are skincare consultations, during which licensed estheticians assess individual skin types and concerns, offering tailored advice on routines and treatments. To ensure a flawless match between makeup and personal coloring, color matching services are also available, helping guests discover the most flattering shades for foundation, blush, and lipstick based on their unique complexion, eye color, and undertones. These services combine luxury, expertise, and attention to detail, allowing visitors to feel rejuvenated and confident throughout their journey.</p>

- Make sure newly created pages are integrated into site via relevant hyperlinks from other pages, or adding into footer or navigation for high value pages.

- If you are recommending a specific place, dish, activity then use Tavily search to research and make sure it really is available at that location, and having found it get some specifics such as company names, restaurant names, addresses, prices, opening hours etc where that place, dish, activity etc is available. Store verbatim Tavily search results into the .private folder with meaningful name for future reference.

- When you find one object at a location do research to find similar or additional. e.g. if you find a beach is mentioned search for more beaches if you have a recommended restaurant, search for more resturants, if you find a famous dish search for more famous dishes, if you find an entrance fee, search for more fees.

- When starting each project make good use of research tools including Tavily search, Google Analytics 4 and Google Search Console (ga4-gsc-mcp). New research should be stored verbatim in the .private folder for future reference.

- Examine and make use of all files in the `.private` folder that might help with a task. Pay attention to the facts file. and the fact checking instructions.

- Constantly strive to make the website even more be impressively informative, meticulously accurate, and clearly superior to its previous version - serving as a reliable resource for travelers.

- Look in the .private folder for youtube transcripts that can contain real user experience information that is useful for local color and detail. If no transcripts found try Tavily search to find youtube videos that are relevant to the topic you are working on, and then use the Tavily Extract tool to extract the material about the video. Store the transcript in the `.private` folder with a meaningful name for future reference.  Use this real user experience to enhance the site by offering "tips" and "recommendations" based on real user experience as well as looking for related topics that real visitors to the location have noticed, perhaps an interesting photo point, a great local cafe, a hidden gem that is not in the guidebooks.

## Localization and Language

- Always write in English but use local terms where appropriate, e.g. "MTR" for the subway in Hong Kong, "RER" for the Paris suburban train system, "S-Bahn" for the Berlin suburban train system, etc.  Local language names can be appended in parentheses, e.g. "MTR (地鐵)".
- Use local currency symbols and formats, e.g. "HK$" for Hong Kong dollars, "€" for Euros, "£" for British pounds.
- Prices should be in the local currency of the location being discussed, e.g. "HK$100" for a restaurant in Hong Kong, "€50" for a museum in Paris, "£20" for a park in London. In US locations use "$" for US dollars. Check the prices are reasonable, as online resources may give prices in US$ and jsut say $, so a resource that just says $ you have to work out is it local currency or US dollars. Use online search or currency converters to verify the local currency and convert prices if necessary.
- Give pronunciation tips for local names, e.g. "MTR (pronounced 'em-tee-are')", "RER (pronounced 'air-air')", "S-Bahn (pronounced 'ess-bahn')", "Ximending (pronounced 'shee-men-ding')"