---
name: kb-query
description: Query the Knowledge Base wiki, synthesize answers with citations, and optionally save valuable Q&A.
---

# kb-query - Knowledge Base Query

Query the Knowledge Base to synthesize answers with proper citations.

## Usage Patterns

- `/kb-query "{question}"` - Ask a question about the knowledge base
- `/kb-query "{topic}" --papers` - Find papers related to a topic
- `/kb-query "{concept}" --deep` - Deep dive into a concept and its relations

## IMA Availability

**IMA_AVAILABLE flag is passed from kb-skill dispatcher (pre-flight check).**

- **If called through kb-skill**: Flag is passed from dispatcher
- **No standalone tool check needed** — use the passed flag

| IMA_AVAILABLE | Method |
|---------------|--------|
| **true** | Primary: IMA KB semantic search |
| **false** | Fallback: File-based search (Glob + Grep + Read) |

---

## Query Process

### Step 1: Search (method depends on IMA_AVAILABLE)

**If IMA_AVAILABLE=true (Primary method - IMA KB search):**

Based on question keywords, search relevant KBs:

```bash
# Search concepts
ima_api "openapi/wiki/v1/search_knowledge" '{"query": "{keyword}", "knowledge_base_id": "concepts_kb_id", "cursor": ""}'

# Search paper summaries
ima_api "openapi/wiki/v1/search_knowledge" '{"query": "{keyword}", "knowledge_base_id": "summary_kb_id", "cursor": ""}'

# Search multiple KBs for comprehensive results
```

- Review `info_list` results for relevant entries
- Check `highlight_content` for matched snippets
- Identify candidate wiki pages and paper summaries

**If IMA_AVAILABLE=false (Fallback - file-based search via _index.md):**

**Step 1a: Grep keywords in category indexes**

For each keyword from the question, search category indexes first (most efficient):

```bash
Grep "{keyword}" wiki/{category}/_index.md
```

Parse matching rows (format: `| [[Name]] | Title | Domain | First Source |`):
- Extract `Name` from wikilink `[[category/Name]]`
- Collect `Title` for relevance assessment
- This returns only matching entries, not entire index

**Step 1b: Read master index if needed**

If no matches in specific categories, check overview:

```bash
Read wiki/_index.md
```

This shows available categories and statistics to guide further search.

**Step 1c: Read matched pages**

Only read specific pages identified from Grep results:

```bash
Read wiki/{category}/{matched_name}.md
```

For paper summaries, Grep in `source/summary/` directory:

```bash
Grep "{keyword}" source/summary/*.md
```

**Why Grep-first approach**:
- `_index.md` contains structured metadata in table format
- Grep returns only rows matching keywords (token-efficient)
- Read entire file only when comprehensive overview needed
- Pattern: Grep → identify candidates → Read specific pages

### Step 2: Page Read

1. Read identified wiki pages using Read tool
2. For detailed findings, read relevant paper summaries in `source/summary/`
3. Collect key findings and track [[citations]] for each piece of information

### Step 3: Synthesis

Synthesize a coherent answer using information from multiple sources.

**Answer structure:**
```markdown
{Main answer synthesizing information}

**Key points:**
- Point 1 with citation [[concepts/{concept}]]
- Point 2 with citation [[source/summary/{citekey}]]

Sources:
- [[concepts/{concept}]] - {what it contributed}
- [[source/summary/{citekey}]] - {specific finding cited}
```

### Step 4: Auto-Suggest Save

After answering, evaluate whether to suggest saving:

**Trigger criteria (multi-factor):**
- Answer references 3+ wiki pages
- Answer synthesizes across categories (concepts + proxies)
- Answer is 150+ words
- User asks follow-up questions

If criteria met, suggest:
```
💡 This answer synthesizes knowledge from multiple sources.
   Save to source/conversations/theme_{YYMMDD}.md?
   Reply "yes" to save, or continue with follow-up questions.
```

## --papers Mode

Find relevant paper summaries related to topic.

**IMA method:**
```bash
ima_api "openapi/wiki/v1/search_knowledge" '{"query": "{topic}", "knowledge_base_id": "summary_kb_id", "cursor": ""}'
```

**Fallback:** Glob `source/summary/*.md` and Grep for topic keyword.

## --deep Mode

For deep dive on a concept:
1. Read the concept page
2. Read all linked theories and proxies
3. Read paper summaries that define/use this concept
4. Synthesize comprehensive overview

## Conversation Save Process

If user confirms, create `source/conversations/theme_{YYMMDD}.md` with question, answer, and sources. Append entry to `wiki/log.md`.

## Important Notes

- Always use [[citations]] for claims
- Don't fabricate information not in wiki
- If information missing, note as gap
- Suggest follow-up questions when appropriate
