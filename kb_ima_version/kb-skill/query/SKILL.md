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

## IMA Knowledge Base Check

Before querying, verify IMA KBs exist:

```bash
ima_api "openapi/wiki/v1/search_knowledge_base" '{"query": "", "cursor": "", "limit": 20}'
```

Required KBs: `summary`, `concepts`, `variables`, `methods`, `constructs`, `theories`

**If KBs missing**: Fall back to file-based search (see below).

## Query Process

### Step 1: Search via IMA

**Primary method (IMA KB available):**

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

**Fallback (IMA KB not available):**

1. Read `wiki/_index.md` to understand available categories
2. Grep for keyword in relevant category: `Grep "{keyword}" wiki/{category}/*.md`
3. Read matched pages

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
