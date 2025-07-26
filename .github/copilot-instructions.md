Always use mcp servers to do research.

If mcp servers timeout then backoff a random 30 to 60 seconds using `sleep`

Always refer to GA4 and GSC data for insights using the ga4-gsc-mcp server

Always use tavily to do research on things you don't know. Never invent or presume, always research with search and extract tooks.

Make use of KeywordsEverywhere mcp server to prioretize money and search volume.

Log everything you do, write logs in the `.private` folder.

When starting a job always look at the `.private/last-job` file to see what was the last job done and what needs to be done next.

When writing code, always use the `.private` folder to store your code snippets and scripts.  Use it to check current status, recent work and so on to avoid duplicating effort.

When editing html pages always stay within the "editableRegion"s if they exist.

Changes to webpages that use templates with editableRegions should be done only in the template .dwt file mentioned in the header of the html.

Use shell scripts .sh and sed, awk etc to do bulk edits, don't do them using diffs.  Example, updating copyright notice on all pages.

When creating new pages always use `cp <templatename>.dwt <new-filename>.html`

If you make a mistake and then correct yourself updated these instructions in the `.github/copilot-instructions.md` file.

When you finish a job, update the `.private/last-job` file with the details of what you did and what needs to be done next.

Always check your work, don't presume that things you have done worked correctly, particularly edits and the use of bash shell commands. Look at the files to confirm changes occurred as expected.