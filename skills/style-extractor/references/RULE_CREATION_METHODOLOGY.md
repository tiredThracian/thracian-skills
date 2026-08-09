# Rule Creation Methodology & Architecture Guide

Derived from enterprise defense and software engineering rule specifications (e.g. `aselsan-know-how-transferi`), this document outlines the exact methodology for creating deterministic, bulletproof Antigravity workspace rules (`.gemini/config/rules/*.md` and `.agent/rules/*.md`).

---

## 1. Core Rule File Architecture & Metadata

Every rule file MUST begin with standard YAML frontmatter defining its description and trigger status, followed by a clear, normative title:

```markdown
---
description: [Clear, single-sentence summary of the rule's domain and mandate]
trigger: always_on  # Options: always_on | manual
---

# [Rule Title in Title Case or Turkish Başlık Formatı]

[Short introductory paragraph stating the scope and mandatory nature of the rule.]
```

---

## 2. The 5 Structural Elements of Effective Rules

To eliminate AI ambiguity and guarantee compliance, rules synthesized by `style-extractor` MUST incorporate five structural elements:

### Element 1: RFC 2119 Normative Imperatives
Use bold, capitalized normative keywords in English or Turkish to establish priority:
- **English:** **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **NEVER**.
- **Turkish:** **ZORUNLUDUR**, **YASAKTIR**, **TERCİH EDİLMELİDİR**, **ASLA**.

### Element 2: Do's and Don'ts Contrast Examples (Yanlış vs. Doğru Kullanımlar)
Every terminology or formatting rule MUST include paired contrasting examples showing exact incorrect patterns alongside correct implementations:

```markdown
### ❌ Yanlış Kullanımlar (Incorrect):
- Sinyal işleme ısınma (warmup) algoritması. (Parantez içi çeviri okunabilirliği düşürür)
- Sıkıştırma motoru / Oturum motoru. (Mecazi "engine/motor" kullanımı yapaydır)

### ✅ Doğru Kullanımlar (Correct):
- Sinyal işleme ısınma algoritması.
- Sıkıştırma mekanizması / Oturum altyapısı.
```

### Element 3: Banned & Mandatory Terminology Matrix
Explicitly list prohibited terms (forced translations, AI clichés, or ambiguous jargon) alongside mandatory domain-approved equivalents:

| Prohibited / Banned Term (Yasaklı) | Mandatory Replacement (Doğru/Zorunlu) | Context / Rationale |
| :--- | :--- | :--- |
| **tampon / tamponlama** | **buffer / bufferlama** | Forced translation creates technical ambiguity. |
| **orkestre etmek** | **yönetmek / koordine etmek** | Overused metaphorical AI cliché. |
| **kilit / kilitlenmesiz** | **lock / lock-free** | Use native concurrency terminology. |
| **günlük / hata günlüğü** | **log / log dosyası** | Standard industry convention. |
| **dijital** | **sayısal** | Official technical standard (sayısal telsiz, sayısal demodülatör). |

### Element 4: Hard Negative Constraints (Syntactic & Tooling Restrictions)
Establish strict operational boundaries preventing unwanted AI behaviors (e.g. no line numbers in code links `#L123`, no unrequested git pushes, no horizontal lines `---` breaking Pandoc Word converters, no mock synthetic data generation without explicit request).

### Element 5: Ground Truth & Verification Requirements (Single Source of Truth)
Define explicit verification steps requiring the AI agent to cross-check outputs against authoritative sources (e.g., projenin kaynak kod dosyalarını inceleyerek teyit etmek, veritabanı şemalarıyla birebir eşleştirmek).

---

## 3. Rule Synthesis Pipeline for `style-extractor`

When the user asks to "create rules from documents/codebase", `style-extractor` follows this synthesis pipeline:

1. **Ingestion & Pattern Scanning:** Scans sample documents or codebases for naming patterns, terminology conventions, formatting rules, and technical constraints.
2. **Normative Abstraction:** Extracts implicit guidelines and elevates them to explicit RFC 2119 mandates.
3. **Contrast Generation:** Formulates concrete bad vs. good examples based on observed anti-patterns.
4. **File Packaging:** Emits clean, copy-pasteable Markdown rule files ready for placement in `.gemini/config/rules/` or `.agent/rules/`.
