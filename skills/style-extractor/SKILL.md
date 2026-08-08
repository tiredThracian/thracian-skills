---
name: style-extractor
description: Analyzes user-provided writing samples, documents, or code comments in English or Turkish (Türkçe) to extract stylometric signatures, authorial voice patterns, and syntactic habits. Synthesizes reusable Antigravity SKILL.md style guides or workspace rule files (.gemini/config/rules/*.md) using RFC 2119 imperative rules. Supports Turkish and English native extraction modes (--tr, --en, --auto). Activate whenever the user asks to learn their writing style, extract style rules from sample documents (in Turkish or English), create a style guide from samples, or generate custom authoring rules.
---

# Style Extractor & Voice Cloning Rule Generator Skill (English & Turkish 🇹🇷)

Use this skill to analyze your writing samples (articles, reports, emails, grant applications, code documentation, or essays in **English** or **Turkish / Türkçe**), extract your personal or organizational authoring signature across 6 stylometric dimensions, and generate a **reusable Antigravity Rule file (`.gemini/config/rules/*.md`)** or **Custom Skill Style Guide (`SKILL.md`)**.

---

## 🎯 Native Multi-Lingual Engine (English & Türkçe)

This skill natively supports both **English** and **Turkish (Türkçe)** prose, handling the unique grammatical, morphological, and structural traits of both languages:

*   **🇬🇧 English Stylometrics:** Analyzes active/passive voice, clause subordination, Oxford commas, em-dash breaks, and English AI-sm clichés (*delve, tapestry, testament, foster, landscape*).
*   **🇹🇷 Turkish (Türkçe) Stylometrics:** Analyzes SOV word order vs. inverted sentences (*kurallı vs. devrik cümle*), verb suffix preferences (`-mektedir/-maktadır` vs. `-yor` vs. `-di`), discourse markers (*Nitekim, Öte yandan, Dolayısıyla*), and Turkish AI clichés (*derinlemesine incelemek, mihenk taşı, günümüz dünyasında, sonuç olarak*).

---

## 🎛️ Language Flags & Modes

*   **`--auto`** *(Default)*: Automatically detects whether the sample text is in English, Turkish, or bilingual, and applies the matching analysis matrix.
*   **`--tr` / `--turkish`**: Forces Turkish morphological analysis, Turkish sentence structure rules, and Turkish Anti-AI Purge Matrix.
*   **`--en` / `--english`**: Forces English stylometric extraction and English Anti-AI Purge Matrix.

---

## 📊 6-Dimensional Stylometric Analysis Framework

The analysis engine evaluates samples across six structural dimensions:

1. **Lexical Profile & Vocabulary:**
   - Word complexity, industry jargon density, preferred discourse markers (English: *"Conversely,"*, *"That said,"*; Turkish: *"Nitekim,"*, *"Öte yandan,"*, *"Dolayısıyla,"*).
   - Assertion vs. Hedging ratio (frequency of definitive claims vs. qualifying words).
2. **Syntactic Architecture & Sentence Structure:**
   - Sentence length distribution (short staccato assertions vs. long compound structures).
   - English: Active vs. passive voice ratios.
   - Turkish: Sentence word order (Kurallı SOV: Özne-Nesne-Yüklem vs. Devrik cümle), active/passive verb suffix ratio (`-il/-in`).
3. **Punctuation, Pacing & Visual Formatting:**
   - Usage footprint of em-dashes (`—`), semicolons, parentheses, and Oxford commas.
   - Paragraph density (single-sentence line breaks vs. dense multi-sentence blocks).
   - Formatting emphasis (selective bolding, Markdown tables, inline code, or narrative prose).
4. **Tone, Stance & Cadence:**
   - Perspective: First-person singular (*"I" / "Ben"*), first-person plural (*"We" / "Biz"*), or detached third-person.
   - Formality rating (1–10 scale) and emotional cadence (pragmatic, authoritative, conversational).
5. **Rhetorical Devices & Argumentation:**
   - Hook strategies, problem-solution loops, analogies, and ending structures.
6. **Anti-AI Footprint (AI-sm Purge Matrix):**
   - **English Purge:** Catalogs synthetic cliché terms (*delve, tapestry, testament, foster, landscape, elevate*) and explicitly forbids them.
   - **Turkish Purge (Türkçe Yapay Zeka Kalıpları):** Catalogs overused Turkish AI clichés (*derinlemesine incelemek, büyük bir titizlikle, mihenk taşı, günümüz dünyasında, mozaik, ışık tutmaktadır, sonuç olarak, unutulmamalıdır ki*) and explicitly forbids them.

---

## 📜 Rule Synthesis Targets

Upon analyzing the provided sample text, this skill formats the output into one of two target formats requested by the user:

### Target Option A: Workspace Rule File (`.gemini/config/rules/user_writing_style.md`)
Generates a global or workspace rule file that enforces your style across all AI turns:

```markdown
# User Writing Style & Authorial Voice Rules (Türkçe / English)

## Voice & Tone / Ses ve Ton
- **Stance / Duruş:** [Direct, empirical, pragmatic / Net, somut, uygulamacı]
- **Perspective / Bakış Açısı:** [Biz / We]
- **Formality Level / Resmiyet Seviyesi:** [8/10]

## Imperative Authoring Rules (RFC 2119)
- **MUST / ZORUNLUDUR:** Use active voice and direct sentence openers.
- **MUST NOT / YASAKTIR:** Do NOT use generic AI filler phrases:
  - English: `delve`, `tapestry`, `testament`, `foster`, `landscape`, `pivotal`.
  - Türkçe: `derinlemesine incelemek`, `büyük bir titizlikle`, `mihenk taşı`, `günümüz dünyasında`, `ışık tutmaktadır`, `sonuç olarak`.
- **MUST / ZORUNLUDUR:** Keep paragraph lengths strictly under 3 sentences.
- **NEVER / ASLA:** Do NOT include generic summary conclusions ("In conclusion", "Sonuç olarak", "Özetlemek gerekirse"). End with an actionable next step.
```

---

### Target Option B: Custom Antigravity Skill Style Guide (`SKILL.md`)
Generates a complete standalone skill definition with YAML frontmatter, context triggers, imperative rules, and few-shot calibration exemplars in English or Turkish.

---

## 📚 Deep Research & Methodology References

For the complete 6-dimensional stylometric theory, English/Turkish Anti-AI purge matrices, and voice calibration prompt patterns, refer to:
[STYLOMETRIC_RESEARCH_GUIDE.md](file:///skills/style-extractor/references/STYLOMETRIC_RESEARCH_GUIDE.md)
