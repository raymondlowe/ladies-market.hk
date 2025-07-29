**Instruction:**

You are tasked with creating and maintaining a rigorously fact-checked, high-quality informational website. Begin by scanning all existing HTML content to extract **proposed factual claims**—such as locations, activities, services, events, and amenities—while filtering out opinions, subjective language, or promotional content.  

In the `.private` directory, create a **fact file** named `facts.xml` using XML format. The first entry must be a well-structured **example** written in **BNF-like syntax** to illustrate acceptable formats and required fields.  

```
<?xml version="1.0" encoding="UTF-8"?>
<!--
BNF Grammar for Fact File Structure:

<fact-file> ::= "<facts>" <fact>* "</facts>"
<fact> ::= "<fact id=\"" <id> "\">" 
           <fact-statement> 
           <source> 
           <category> 
           <fact-check-status> 
           <verification-details>? 
           <metadata> 
           "</fact>"

<id> ::= <string>                    <!-- Unique identifier -->
<fact-statement> ::= "<statement>" <text> "</statement>"
<source> ::= "<source>" <url-or-file> "</source>"
<category> ::= "<category>" ( "geography" | "food" | "culture" | "transportation" | "events" | "accommodation" | "recreation" | "history" | "economy" ) "</category>"
<fact-check-status> ::= "<status>" ( "unverified" | "verified" | "false" | "partially-true" | "disputed" ) "</status>"
<verification-details> ::= "<verification>" 
                          <verification-url>? 
                          <date-checked> 
                          <checked-by> 
                          <confidence-level> 
                          <notes>? 
                          "</verification>"
<metadata> ::= "<metadata>" 
               <created-date> 
               <last-updated> 
               <importance-level> 
               <tourist-relevance> 
               "</metadata>"

```

Adjust the XML structure as necessary, adding new fields and tags that are relevant to this case is fine. The XML structure is a framework, not a iron clad rule.

 Use **Tavily Search and Extract** to independently verify every proposed fact. Update the XML file with:  
 - Verified `citation_url` from authoritative sources  
 - Accurate `date_checked` (use current system date; correct any outdated entries)  
 - Appropriate `status` based on verification outcome  

 Expand your research to ensure comprehensive coverage:  
 - Include **all named restaurants** or similar things such as **shops**, **museums**, **businesses**, verifying existence, cuisine, availability (especially during events like the Bun Festival)  
 - Cover **beaches** or similar such as **parks**, **promenades**, **photo locations**, including names, accessibility, facilities, safety  
 - Include **recreational activities** (e.g., windsurfing, kayaking, bike rentals, wine tasting, people watching)  
 - Verify **event dates, durations, and cultural significance**  
 - Add any other tourist-relevant categories missing from initial scans  

 After completing the fact-checking phase, use the verified `facts.xml` and supporting research files in `.private` to **enhance the website**:  
 - Edit, rewrite, and expand pages for accuracy, depth, and usefulness  
 - Add new sections or pages where gaps exist  
 - Ensure content is detailed, engaging, and helpful—transforming raw facts into compelling, trustworthy visitor guidance  
 - It is good to express opinion, but combine them or use them as an adjunct to facts  
 - Prioritize high CPC terms, topics with a good combination of high volume and moderate competition.
 - In your writing focus on readability, clarity, structure, and user experience. Use full evocative sensorial language, write full expressive paragraphs but keep vocabulary to middle school level. Break up walls of text with call out boxes, "tips", "recommendations" etc as well as lists, emojis and links to other resources both internal and external.

 The final website edots should make the site even more be impressively informative, meticulously accurate, and clearly superior to its previous version—serving as a reliable resource for travelers.
