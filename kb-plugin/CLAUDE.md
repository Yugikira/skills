# Overview

Vercel open sourced a embedding free [`Knowledge Agent`](https://github.com/vercel-labs/knowledge-agent-template) with a [promotion article](https://vercel.com/blog/build-knowledge-agents-without-embeddings). The **object** of this project is to replicate the `Knowlege Agent` that can implemented in Claude Code, without other sophisticated features such as Progres database, Vercel Sandbox, etc.

# The Role of the Agent or Skill

The first version of the `Knowledge Agent` is designed to perform domain-specific, which targeted on economics, finance and accounting, knowledge base building, performing query and summarization, and self-evolving.

# Basic Abilities

The `Knowledge Anget` or skill is supposed to have following abilities:

- Organize pdf papers that user put in ./raw/data/. The organization could be perform with a skill called [`libby-extract`](../libby/extract/SKILL.md).

- Agent then can convert the `pdf` file to `markdown` with  a skill called [`paddle-pdf`](../paddle-pdf/SKILL.md). 

- Extract findings, concepts (including definition of the concepts), measures/proxies (practical represent of concepts) and update markdown files to form a wiki (within ./wiki/).

    - Use `Obsidian`'s method to organize the md files, use [[filename]] to linking files. 

- Maintain an _index.md file for further quickly query or search where to find information through `find`, `cat`, `grep` and so on `Bash` commands.

- Write summary of each paper (put in ./source/summary) with refer to a template (provide latter). And the wiki could also refer to these summaries. 

- After querying tasks or discussion with user, extract key question-answers that are valuable to the Knowledge base, write a summary with name `conversation_theme_yymmdd.md` in ./source/conversations/.

- If user ask "explain paper {title}/{doi}" or "add paper {title}/{doi} to our knowledge base/wiki", agent can use [`libby fetch`](../libby/fetch/)(if provided with doi), or `libby extract {title}` first and then `libby fetch doi` with the information from `libby extract`. Then perform a typical process. Warning user to provide the paper, if the previous work fails. 

# Other references

- This idea is somehow generated from [Kaparthy's llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), you can refer to the article for more thoughts.

- Some people already implement and open-source the Karparthy's llm-wiki:

    - [llm-wiki-skill](https://github.com/lewislulu/llm-wiki-skill)
    - [wiki-skills](https://github.com/kfchou/wiki-skills)

# Other Creation Criteria

- Use skill-creator skill if you decide a skill is well-suited.

- I prefer separate sub-skills/sub-agents to save tokens and to prevent context rot.

- The agents/skills is designed for Claude Code with highest priority.

- Current folder is the working folder, **DON'T"** create a `skills/` folder.

- If you find `python` scripts with **ONLY** standard library is helpful in saving tokens/getting job done, write it and put it in ./Scripts/.

# Available Skills

The Knowledge Agent provides four skills for managing the knowledge base:

- **kb-ingest**: `/kb-ingest {doi|title|citekey}` - Ingest papers into the knowledge base
- **kb-query**: `/kb-query "{question}"` - Query and synthesize answers from wiki
- **kb-lint**: `/kb-lint [--quick|--contradictions]` - Health check for wiki

Internal helper (not user-invocable):
- **kb-extract**: Called by kb-ingest to extract knowledge from papers

## Quick Start

1. Drop PDFs into `raw/data/`
2. Run `/kb-ingest --batch` to process all
3. Run `/kb-query "your question"` to query the wiki
4. Run `/kb-lint` periodically to maintain health

## Wiki Structure

- `wiki/concepts/` - Concept definitions and relationships
- `wiki/constructs/` - Theoretical constructs from analytical models (model parameters, definitional constructs)
- `wiki/theories/` - Theoretical frameworks
- `wiki/variables/` - Measures and operationalizations
- `wiki/methods/` - Research methodologies
- `source/summary/` - Paper summaries
- `source/conversations/` - Saved Q&A discussions

## Templates

All wiki pages use templates in `templates/`:
- `paper_summary.md` - Paper summary with 3-tier findings structure
- `concept.md`, `theory.md`, `variable.md`, `method.md`, `construct.md` - Wiki page templates
- `method_analytical.md` - Template for analytical/mathematical models
