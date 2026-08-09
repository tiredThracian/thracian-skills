---
name: style-extractor
description: Analyzes user-provided writing samples, codebase conventions, or manually created rules (in English or Turkish) to extract stylometric signatures, authorial voice patterns, and general-purpose rule discovery patterns. Synthesizes deterministic Antigravity rule files (.gemini/config/rules/*.md or .agent/rules/*.md) and custom SKILL.md style guides using RFC 2119 imperative rules, Do's/Don'ts tables, and terminology matrices. Activate whenever the user asks to learn their writing style, extract style rules, discover rule patterns from example documents/codebases, or generate custom authoring rules.
---

# Style Extractor & Rule Pattern Discovery Skill (English & Turkish 🇹🇷)

Use this skill to analyze writing samples, codebases, or manually created rules (in **English** or **Turkish / Türkçe**), discover underlying authoring patterns or domain boundaries, and generate **reusable Antigravity Rule files (`.gemini/config/rules/*.md` / `.agent/rules/*.md`)** or **Custom Skill Style Guides (`SKILL.md`)**.

---

## 🎯 Dual Workflows: Style Cloning vs. Rule Pattern Discovery

This skill supports two primary output generation workflows:

```text
               ┌────────────────────────────────────────────────────────┐
               │    INPUT: Writing Samples / Manual Rules / Codebase    │
               └───────────────────────────┬────────────────────────────┘
                                           │
                ┌──────────────────────────┴──────────────────────────┐
                ▼                                                     ▼
    [WORKFLOW 1: Style & Voice Cloning]                 [WORKFLOW 2: Rule Pattern Discovery]
    Outputs: User Voice SKILL.md                        Outputs: .gemini/config/rules/*.md
    Focus: 6D Stylometrics & Cadence                    Focus: Pattern Discovery, RFC 2119 Directives,
                                                               Terminology Maps & Ground Truth Verification
```

---

## 🔍 Rule Pattern Discovery Methodology

When analyzing manually created rules or sample documents to formulate new general-purpose rules, this skill applies a 5-part pattern discovery framework:

### 1. Absolute Boundary Directives (Hard Constraints)
*   **Discovery Method:** Scans manual rules for non-negotiable mandates, file placement rules, or workflow restrictions.
*   **Formulation:** Converts patterns into explicit RFC 2119 imperatives (**MUST** / **ZORUNLUDUR** or **MUST NOT** / **YASAKTIR**).

### 2. Terminology Preference & Synonym Normalization Maps
*   **Discovery Method:** Identifies terms the author consistently replaces, bans, or prefers over default LLM vocabulary.
*   **Formulation:** Builds a 2-column or 3-column **Terminology Matrix** mapping prohibited terms to canonical approved equivalents.

### 3. Negative Constraints & Anti-Pattern Flags
*   **Discovery Method:** Identifies prohibitions against default AI tendencies (e.g. over-explanation, parenthetical translations, fluff intros, unrequested git actions, static line numbers).
*   **Formulation:** Formulates explicit **MUST NOT** / **NEVER** / **YASAKTIR** negative directives paired with concrete "Do's and Don'ts" (Yanlış vs. Doğru) contrast examples.

### 4. Structural & Formatting Signatures
*   **Discovery Method:** Analyzes document layouts for recurring markup tags, custom annotations, specific table structures, or header capitalization rules.
*   **Formulation:** Defines exact syntax constraints and structural templates.

### 5. Ground Truth & Verification Requirements
*   **Discovery Method:** Identifies directives requiring the AI to cross-check outputs against primary authoritative sources (code, schemas, specs).
*   **Formulation:** Adds a mandatory **Verification Directives** section enforcing empirical cross-checking before declaring task completion.

---

## 🎛️ Language Flags & Modes

*   **`--auto`** *(Default)*: Automatically detects sample language (English, Turkish, or Bilingual) and applies matching analysis.
*   **`--tr` / `--turkish`**: Applies Turkish morphosyntactic analysis, Turkish RFC 2119 terms (**ZORUNLUDUR**, **YASAKTIR**), and Turkish Anti-AI Purge Matrix.
*   **`--en` / `--english`**: Applies English stylometrics and English Anti-AI Purge Matrix.

---

## 📜 Rule File Synthesis Format

Rules generated for `.gemini/config/rules/` or `.agent/rules/` follow this domain-agnostic structure:

```markdown
---
description: [Single-sentence summary of the rule's mandate]
trigger: always_on  # Options: always_on | manual
---

# [Rule Domain Title]

[Brief statement of scope and operational intent.]

## 1. Mandatory Directives
- AI agents **MUST / ZORUNLUDUR** [core directive].
- AI agents **MUST NOT / YASAKTIR** [prohibited action].

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
AI agents **MUST** verify all generated claims against primary source files before completing the task.
```

---

## 📚 Methodological References

- For the general Rule Pattern Discovery Framework, see:  
  [RULE_CREATION_METHODOLOGY.md](file:///skills/style-extractor/references/RULE_CREATION_METHODOLOGY.md)
- For 6D stylometric theory and voice cloning prompt patterns, see:  
  [STYLOMETRIC_RESEARCH_GUIDE.md](file:///skills/style-extractor/references/STYLOMETRIC_RESEARCH_GUIDE.md)
