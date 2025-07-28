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