# Rule Pattern Discovery & Extraction Meta-Methodology

This guide defines the meta-methodology for analyzing manually created rules or sample documents to discover, extract, and formulate new reusable workspace rules (`.gemini/config/rules/*.md` or `.agent/rules/*.md`) without hardcoding rigid templates.

---

## 🎯 Architectural Goal

The objective of rule pattern discovery is to analyze an author's or organization's manually written rules/samples and identify **underlying structural patterns, boundary constraints, and terminology preferences**, elevating them into clean, general-purpose rules.

```text
               ┌────────────────────────────────────────────────────────┐
               │    INPUT: Manually Created Rules & Sample Documents    │
               └───────────────────────────┬────────────────────────────┘
                                           │
                ┌──────────────────────────┴──────────────────────────┐
                ▼                                                     ▼
   [PATTERN RECOGNITION & ANALYSIS]                  [GENERALIZED RULE FORMULATION]
   - Scan for Absolute Constraints                   - Convert to Direct Imperatives
   - Detect Anti-Patterns & Prohibitions             - Build Terminology Mapping Tables
   - Identify Formatting Signatures                  - Formulate Contrast (Do/Don't) Examples
   - Extract Verification Criteria                   - Generate Standard Rule Files
```

---

## 🔍 5 Core Rule Patterns & How to Discover Them

When inspecting manually created rules or sample documents, look for these 5 foundational pattern types:

### Pattern 1: Absolute Boundary Directives (Hard Constraints)
*   **How to Discover:** Search manual samples for non-negotiable directives, strict placement requirements, or workflow limits (e.g., *"always save in X"*, *"never generate Y unless explicitly requested"*, *"must match Z 100%"*).
*   **Rule Formulation Method:** Translate into direct, clear imperative statements (*"X is required"*, *"Y is prohibited"*). State the exact constraint and why it matters.

### Pattern 2: Terminology Preference & Synonym Normalization Maps
*   **How to Discover:** Compare the author's chosen terms against generic LLM defaults or literal translations. Identify terms the author consistently replaces, bans, or prefers.
*   **Rule Formulation Method:** Create a 2-column or 3-column **Terminology Matrix** mapping prohibited terms directly to canonical approved equivalents, along with contextual rationales.

| Prohibited / Banned Term | Mandatory Canonical Replacement | Context / Rationale |
| :--- | :--- | :--- |
| `[Prohibited Cliché or Ambiguous Term]` | `[Author's Approved Term]` | Prevents ambiguity or artificial phrasing. |

### Pattern 3: Negative Constraints & Anti-Pattern Flags
*   **How to Discover:** Look for explicit prohibitions against default LLM tendencies (e.g. over-explanation, parenthetical translations, fluff intros, unrequested git actions, static line numbers).
*   **Rule Formulation Method:** Formulate explicit negative directives paired with concrete "Do's and Don'ts" (Yanlış vs. Doğru) contrast examples.

### Pattern 4: Structural & Formatting Signatures
*   **How to Discover:** Analyze document layouts for recurring markup tags, custom annotations, specific table column layouts, header capitalization rules, paragraph density caps, or custom annotation syntax.
*   **Rule Formulation Method:** Document the exact syntax pattern and header/paragraph rules that the AI must replicate in all generated text.

### Pattern 5: Ground Truth & Verification Requirements
*   **How to Discover:** Search for instructions requiring the AI agent to verify claims against authoritative primary sources (e.g. source code, database schemas, hardware specs) rather than relying on memory or templates.
*   **Rule Formulation Method:** Include a clear **Verification Directives** section enforcing empirical cross-checking before declaring compliance.

---

## 📜 Standard Rule File Format

When pattern discovery is complete, package the extracted rules into a standardized Antigravity rule file:

```markdown
---
description: [Single-sentence summary of the rule's mandate]
trigger: always_on  # Options: always_on | manual
---

# [Rule Domain Title]

[Brief statement of scope and operational intent.]

## 1. Mandatory Directives
- [Core directive statement].
- [Prohibited action statement].

## 2. Terminology & Prohibited Words Matrix

| Prohibited Term | Approved Equivalent | Rationale |
| :--- | :--- | :--- |
| `[banned_term]` | `[approved_term]` | [Why banned] |

## 3. Do's and Don'ts Contrast Examples

### ❌ Incorrect (Yanlış Kullanım):
> [Example demonstrating the anti-pattern]

### ✅ Correct (Doğru Kullanım):
> [Example demonstrating the compliant pattern]

## 4. Ground Truth Verification Requirement
[Directive requiring empirical verification against primary source files before completing the task.]
```
