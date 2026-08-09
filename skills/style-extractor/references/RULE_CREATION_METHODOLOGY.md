# Comprehensive Enterprise Rule Creation Methodology & Architecture Guide

Derived from production defense software engineering standards in `D:\Work\Projekts\aselsan-know-how-transferi`, this document details the complete methodology for creating deterministic, bulletproof Antigravity workspace rules (`.gemini/config/rules/*.md` and `.agent/rules/*.md`).

---

## 1. Core Rule File Architecture & Metadata

Every rule file MUST begin with clean YAML metadata and a clear normative title:

```markdown
---
description: [Clear, single-sentence summary of the rule's domain and mandate]
trigger: always_on  # Options: always_on | manual
---

# [Normative Rule Title in Title Case or Türkçe Başlık Formatı]

[Short introductory paragraph stating the scope and mandatory nature of the rule.]
```

---

## 2. The 7 Enterprise Rule Categories

Rules created by `style-extractor` are categorized into 7 structural domains:

```text
                                 ┌───────────────────────────────────────────────┐
                                 │     ENTERPRISE RULE CREATION METHODOLOGY      │
                                 └───────────────────────┬───────────────────────┘
                                                         │
   ┌─────────────────┬───────────────────┼───────────────┴───┬───────────────────┬───────────────────┐
   ▼                 ▼                   ▼                   ▼                   ▼                   ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Ground      │ │ Terminology  │ │ Document     │   │ Caption &    │    │ Scripting &  │    │ Project-     │
│  Truth Code  │ │ & Language   │ │ Naming &     │   │ Compiler     │    │ Escaping     │    │ Specific     │
│  Reference   │ │ Regulations  │ │ Hierarchy    │   │ Syntax       │    │ Safety       │    │ System Rules │
└──────────────┘ └──────────────┘ └──────────────┘   └──────────────┘    └──────────────┘    └──────────────┘
```

### 1. Ground Truth Code Reference Check (`codebase_reference_check.md`)
- **Single Source of Truth:** Source code (C++, C#, Java, Python) is the primary reference. AI agents **MUST NOT** rely solely on templates or memory.
- **Verification Directives:** Function signatures, member variables, database tables/columns (`Int64`, `DateTime`), protocol headers, and log messages **MUST** be verified directly from source code files.
- **Semantics & Body Verification:** Agents **MUST NOT** infer function behavior from function names alone. Function bodies **MUST** be inspected (mutexes locked, sub-functions called, logs written).

### 2. Terminology & Language Regulations (`documentation_language.md`)
- **No Parenthetical Translations:** Inline translations like `Header (Başlık)` or `warmup (ısınma)` are **FORBIDDEN** (okunabilirliği düşürür).
- **Prohibited Words Matrix:** Explicit bans on forced translations or generic metaphoric terms (*"tampon/tamponlama" ➔ use "buffer/bufferlama"*, *"orkestre etmek" ➔ use "yönetmek"*, *"dijital" ➔ use "sayısal"*, *"gösterici" ➔ use "pointer"*).
- **No Line Numbers in Links:** Links to code files **MUST NOT** include static line numbers (`#L123`) which drift over time.

### 3. Document Naming, Placement & Hierarchy (`document_naming_and_placement.md`)
- **Naming Pattern:** `[TYPE]_[PROJECT].docx` in upper case (e.g. `YTET_LENS.docx`, `YGO_IRIS.docx`). Status suffixes (`_Nihai`, `_v1.0`) are **FORBIDDEN**.
- **Placement:** All output documents **MUST** be saved in `[Project]/docs/`. Root-level placement is forbidden.
- **Header Alignment:** `#` depth MUST equal header numbers (`# 1.`, `## 1.1`, `### 1.1.1`). H1 headers MUST be ALL CAPS.

### 4. Caption & Compiler Syntax (`captions.md`)
- **Table Captions:** Mandatory `%% table_caption: [Description]` on the line directly preceding Markdown tables.
- **Image Captions:** Mandatory `%% static_image: [Description]` tag for images.
- **Mermaid Captions:** Mandatory `%% caption: [Description]` inside the first line of Mermaid blocks, with special character escaping (`""`) and mindmap shape rules.
- **No Horizontal Dividers:** Raw horizontal rules (`---`) in body markdown are **FORBIDDEN** (breaks Pandoc Word compilers).

### 5. Scripting & Escaping Safety (`xml_html_writing_safety.md`)
- **XML/HTML String Safety:** In Python generators, raw `<Tag>` strings are **FORBIDDEN** to prevent rich-text parser corruption (`[[ORCA_RICH_MD...]]`). Escaping placeholders (`LT`/`GT`) **MUST** be used and replaced prior to file output.

### 6. Project & System-Specific Rules (`ytet_project_rules.md`)
- **Specific Term Bans:** Generic terms (*"uygulama"*, *"program"*, *"yazılım"*) are **FORBIDDEN**. The official system configuration unit name (e.g., **`İRİS`**) **MUST** be used.
- **4-Column Test Tables:** Mandatory `| Adım No | Adım Tanımı | Beklenen Sonuç | Doğrulanan Gereksinim(ler) |` table structure.
- **No Parameter Bullet Items:** Parameter blocks must be unbulleted bold paragraphs (`**ID:** YTET-01-01`).

### 7. Document Content Conformance (`document_content_conformance.md`)
- **Traceability & Completeness:** Every requirement or item in normative templates MUST be satisfied or explicitly justified as `Uygulanamaz` with evidence. Silent omission is **FORBIDDEN**.
- **Cross-Document Terminology Alignment:** Unit names, classes, interfaces, and architecture diagrams MUST match 100% identically across document sets (YGO, YTT, YTET, YTER, YUO).

---

## 3. RFC 2119 Normative Imperatives Summary

Rules created by `style-extractor` MUST encode directives using bold normative keywords:
- **Turkish:** **ZORUNLUDUR** (MUST), **YASAKTIR** (MUST NOT / FORBIDDEN), **TERCİH EDİLMELİDİR** (SHOULD), **ASLA** (NEVER).
- **English:** **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **NEVER**.

---

## 4. Synthesis Output Pattern

Rules generated for `.gemini/config/rules/` or `.agent/rules/` follow this structure:

```markdown
---
description: [Single-sentence mandate summary]
trigger: always_on
---

# [Domain/Rule Title]

## 1. Directives & Mandates
- AI agents **ZORUNLUDUR / MUST** [directive].
- AI agents **YASAKTIR / MUST NOT** [prohibited action].

## 2. Terminology & Prohibited Words Matrix

| Yasaklı Terim (Prohibited) | Doğru / Zorunlu Karşılık (Mandatory) | Rationale |
| :--- | :--- | :--- |
| `[banned_1]` | `[approved_1]` | [Reason] |

## 3. Do's & Don'ts Examples

### ❌ Yanlış Kullanım (Incorrect):
> [Bad example]

### ✅ Doğru Kullanım (Correct):
> [Good example]

## 4. Ground Truth Verification Requirement
AI agents **MUST** verify all claims directly against source code files or database schemas.
```
