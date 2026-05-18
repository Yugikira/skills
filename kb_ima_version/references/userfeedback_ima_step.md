# Suggested Improvements for kb-skill/ingest/SKILL.md Phase 7

**Context:** During kb-ingest execution, the agent skipped Phase 7 (IMA KB Sync) assuming IMA tool was unavailable, without actually checking if the tool existed. The ima-skill was later added and files were successfully uploaded.

**Root Cause:** The instruction said "check KB availability" but agent interpreted this as "if I'm not sure, skip." Missing explicit rules about mandatory tool-checking before skip decisions.

---

## Suggestion 1: Add Pre-Phase 7 Tool Availability Check

**Current (Step 1):**
```markdown
**Step 1: Check IMA KB Availability**

```bash
ima_api "openapi/wiki/v1/search_knowledge_base" '{"query": "", "cursor": "", "limit": 20}'
```
```

**Suggested (Add before Step 1):**

```markdown
### Phase 7: IMA Knowledge Base Sync

⛔ **MANDATORY: DO NOT SKIP THIS PHASE** 

Before deciding whether to proceed, you MUST verify IMA tool availability:

**Pre-Step 0: Verify IMA Tool Exists**

```bash
# Check if ima_api CLI is available
node .claude/skills/ima-skill/ima_api.cjs --help 2>/dev/null || echo "IMA tool not found"
```

OR check if ima-skill exists:

```bash
ls .claude/skills/ima-skill/ima_api.cjs
```

**Decision Flow:**

| Condition | Action |
|-----------|--------|
| `ima_api.cjs` EXISTS | **PROCEED** to Step 1 (check KB availability) |
| `ima_api.cjs` NOT FOUND | **DO NOT SKIP** — Prompt user: "IMA skill not configured. To enable IMA sync, please install ima-skill plugin." |

**❌ WRONG:** Assuming IMA is unavailable and skipping Phase 7 without checking.
**✅ CORRECT:** Attempt tool check first; only prompt user if tool genuinely missing.
```

---

## Suggestion 2: Make Skip Conditions Explicit

**Add at the top of Phase 7:**

```markdown
### Phase 7: IMA Knowledge Base Sync

⚠️ **This phase is NOT optional.** Skipping is ONLY allowed when:

1. `ima_api.cjs` file does not exist (tool not installed)
2. User explicitly says "skip IMA sync"

**You MUST attempt the following check before any skip decision:**

```bash
# REQUIRED: Check tool availability before skipping
ls .claude/skills/ima-skill/ima_api.cjs 2>/dev/null
```

If file exists → Proceed with Steps 1-7
If file missing → Prompt user (do not silently skip)
```

---

## Suggestion 3: Add Decision Tree Diagram

```markdown
### Phase 7: IMA Knowledge Base Sync

**Decision Tree:**

```
┌─────────────────────────────────────┐
│ ls .claude/skills/ima-skill/ima_api.cjs │
└─────────────────────────────────────┘
           │
           ▼
    ┌──────────────┐
    │ File exists? │
    └──────────────┘
      │         │
     YES        NO
      │         │
      ▼         ▼
┌──────────┐  ┌──────────────────────────────┐
│ PROCEED  │  │ PROMPT USER:                 │
│ to Step 1│  │ "IMA skill not installed.     │
└──────────┘  │ Install ima-skill to sync."  │
              │ DO NOT silently skip.        │
              └──────────────────────────────┘
```

**Step 1: Check IMA KB Availability** (only if tool exists)

```bash
node .claude/skills/ima-skill/ima_api.cjs "openapi/wiki/v1/search_knowledge_base" '{"query": "", "cursor": "", "limit": 20}'
```
```

---

## Suggestion 4: Add Rule to Skill Header

In the main `kb-skill/SKILL.md` header section, add:

```markdown
## Phase Execution Rules

| Phase | Skip Allowed? | Condition |
|-------|---------------|-----------|
| Phase 1-6 | No | Always execute |
| Phase 7 (IMA Sync) | No* | *Only if tool missing - must verify first |

**Before skipping Phase 7:** Run `ls .claude/skills/ima-skill/ima_api.cjs` — if file exists, proceed with sync.
```

---

## Summary of Key Changes

| Problem | Fix |
|---------|-----|
| Agent assumed skip was OK | Add "⛔ DO NOT SKIP" rule |
| No tool availability check | Add Pre-Step 0: Verify tool exists |
| Unclear when to prompt user | Add explicit decision table |
| No visual guidance | Add decision tree diagram |

---

## Implementation Priority

1. **High**: Suggestion 1 (Pre-Step 0) - prevents silent skipping
2. **Medium**: Suggestion 2 (Explicit skip conditions) - clarifies rules
3. **Low**: Suggestion 3 (Decision tree) - visual aid
4. **High**: Suggestion 4 (Header rules) - sets expectations early

---

## Test Case for Verification

After implementing, verify with this scenario:

**Input:** User runs `/kb-ingest {citekey}` without ima-skill installed
**Expected:** Agent checks for tool → Not found → Prompts user "IMA skill not installed"
**Wrong:** Agent silently skips Phase 7 without checking

**Input:** User runs `/kb-ingest {citekey}` with ima-skill installed
**Expected:** Agent checks for tool → Found → Proceeds to Step 1 (check KB availability)
**Wrong:** Agent skips Phase 7 assuming tool unavailable