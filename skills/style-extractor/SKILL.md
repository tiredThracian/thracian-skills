---
name: style-extractor
description: Analyzes user-provided writing samples, documents, or code comments to extract stylometric signatures, authorial voice patterns, and syntactic habits. Synthesizes reusable Antigravity SKILL.md style guides or workspace rule files (.gemini/config/rules/*.md) using RFC 2119 imperative rules. Activate whenever the user asks to learn their writing style, extract style rules from sample documents, create a style guide from writing samples, or generate custom authoring rules.
---

# Style Extractor & Voice Cloning Rule Generator Skill

Use this skill to analyze your writing samples (articles, reports, emails, grant applications, or code documentation), extract your personal or organizational authoring signature across 6 stylometric dimensions, and generate a **reusable Antigravity Rule file (`.gemini/config/rules/*.md`)** or **Custom Skill Style Guide (`SKILL.md`)**.

---

## 🎯 Purpose & Workflow Overview

When provided with one or more sample documents written by an author or team, this skill executes a 4-stage extraction pipeline:

```text
[1. Sample Analysis] ➔ [2. 6D Stylometric Extraction] ➔ [3. RFC 2119 Rule Formulation] ➔ [4. Rule File / SKILL.md Synthesis]
```

---

## 📊 6-Dimensional Stylometric Analysis Framework

The analysis engine evaluates samples across six structural dimensions:

1. **Lexical Profile & Vocabulary:**
   - Word complexity, industry jargon density, preferred discourse markers (e.g. favoring *"Conversely,"* or *"That said,"* over *"However,"*).
   - Assertion vs. Hedging ratio (frequency of definitive claims vs. qualifying words).
2. **Syntactic Architecture & Sentence Structure:**
   - Sentence length distribution (short staccato assertions vs. long compound structures).
   - Active vs. passive voice ratios.
   - Sentence opening patterns (adverbial fronting, participle clauses, direct subject-verb starts).
3. **Punctuation, Pacing & Visual Formatting:**
   - Usage footprint of em-dashes (`—`), semicolons, parentheses, and Oxford commas.
   - Paragraph density (single-sentence line breaks vs. dense multi-sentence blocks).
   - Formatting emphasis (selective bolding, Markdown tables, inline code, or narrative prose).
4. **Tone, Stance & Cadence:**
   - Perspective: First-person singular (*"I"*), first-person plural (*"We"*), or detached third-person.
   - Formality rating (1–10 scale) and emotional cadence (pragmatic, authoritative, conversational).
5. **Rhetorical Devices & Argumentation:**
   - Hook strategies, problem-solution loops, analogies, and ending structures (e.g. forward-looking takeaway vs. call-to-action).
6. **Anti-AI Footprint (AI-sm Purge Matrix):**
   - Catalogs synthetic cliché terms (*delve, tapestry, testament, foster, landscape, elevate*) that are absent in the author's work and explicitly forbids them.

---

## 📜 Rule Synthesis Targets

Upon analyzing the provided sample text, this skill formats the output into one of two target formats requested by the user:

### Target Option A: Workspace Rule File (`.gemini/config/rules/user_writing_style.md`)
Generates a global or workspace rule file that enforces your style across all AI turns:

```markdown
# User Writing Style & Authorial Voice Rules

## Voice & Tone
- **Stance:** [Direct, empirical, pragmatic]
- **Perspective:** [First-person plural "We" / First-person "I"]
- **Formality Level:** [8/10]

## Imperative Authoring Rules (RFC 2119)
- **MUST** use active voice and direct subject-verb sentence openers.
- **MUST NOT** use generic AI filler words: `delve`, `tapestry`, `testament`, `foster`, `landscape`, `pivotal`.
- **MUST** keep paragraph lengths strictly under 3 sentences.
- **SHOULD** use em-dashes (`—`) to introduce inline technical clarifications.
- **NEVER** include generic summary conclusions ("In conclusion", "To summarize"). End with an actionable next step.
```

---

### Target Option B: Custom Antigravity Skill Style Guide (`SKILL.md`)
Generates a complete standalone skill definition with YAML frontmatter, context triggers, imperative rules, and few-shot calibration exemplars:

```markdown
---
name: [author-or-brand]-voice
description: Enforces the writing style, syntax, and formatting rules of [Author/Brand Name] for all document generation tasks.
---

# [Author/Brand Name] Authoring Style Guide

## Voice & Persona Overview
- **Core Stance:** Direct, analytical, authoritative.
- **Formality Level:** 8/10.

## Imperative Authoring Rules (RFC 2119)

### Lexical & Vocabulary Rules
- **MUST** use domain keywords: [List extracted keywords].
- **MUST NOT** use generic AI terms: `delve`, `tapestry`, `testament`, `foster`, `landscape`.

### Syntactic & Sentence Structure Rules
- **MUST** average [X] words per sentence.
- **MUST NOT** start two consecutive sentences with the same construction.

## Few-Shot Voice Calibration Exemplars

### Exemplar 1: Standard Input to Styled Output

**Standard Draft:**
> [Unstyled baseline text]

**[Author/Brand] Styled Output:**
> [Transformed text matching author's voice]
```

---

## 📚 Deep Research & Methodology References

For the complete 6-dimensional stylometric theory, Anti-AI purge matrices, and voice calibration prompt patterns, refer to:
[STYLOMETRIC_RESEARCH_GUIDE.md](file:///skills/style-extractor/references/STYLOMETRIC_RESEARCH_GUIDE.md)
