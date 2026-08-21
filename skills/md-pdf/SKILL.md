---
name: md-pdf
description: Author, format, and present outputs as dual GitHub-Flavored Markdown (.md) and publication-grade PDF (.pdf) documents with professional typography, code syntax highlighting, tables, callouts, and page numbering. Trigger whenever the user asks for outputs in both MD and PDF, executive reports, research briefings, or document exports.
---

# 📄 Dual Output Skill: Markdown & PDF Publisher (`md-pdf`)

The **`md-pdf`** skill enables the agent to author, format, and deliver all requested documents, reports, proposals, and summaries as **dual outputs**:
1. **Markdown (`.md`)**: Fully structured, clean GitHub-Flavored Markdown for version control, code review, and CLI readers.
2. **Publication-Grade PDF (`.pdf`)**: Print-ready, executive-styled PDF with modern typography (Inter, JetBrains Mono), code syntax highlighting, responsive tables, callout badges, and page numbering.

---

## 🎯 When to Activate

Trigger this skill whenever:
- The user explicitly asks for **dual MD + PDF output** (e.g. *"çıktıları hem md hem de pdf olarak sun"*, *"generate as md and pdf"*, *"export report to pdf and md"*).
- Creating **Executive Reports, Technical Proposals, System Architecture Briefs, or Audit Summaries** where both a developer-readable file and a presentation-ready document are required.
- Converting existing Markdown files into styled PDF documents.

---

## ⚡ Standard 3-Step Execution Workflow

Whenever this skill is engaged, follow these three steps sequentially:

### Step 1: Write the Markdown Document (`.md`)
Create the Markdown document using the `write_to_file` tool.
Include YAML frontmatter at the top of the file to populate metadata:

```markdown
---
title: System Architecture & Security Audit
category: Technical Assessment
author: AI Lead Architect
date: August 21, 2026
---

# Executive Summary

Summary content goes here...

> [!NOTE]
> This assessment highlights key findings and migration paths.

## Performance Benchmark

| Metric | Baseline | Optimized | Gain |
| :--- | :--- | :--- | :--- |
| Latency (p95) | 450ms | 85ms | **5.3x faster** |
| Memory Usage | 2.4 GB | 620 MB | **74% reduced** |

## Implementation Sample

```python
async def handle_request(payload: dict) -> dict:
    return {"status": "ok", "processed": True}
```

<!-- pagebreak -->

## Next Steps
...
```

### Step 2: Generate the PDF via the Conversion Engine
Run the `convert.py` script via `run_command`:

```powershell
python "C:\Users\ibrah\.gemini\config\skills\md-pdf\scripts\convert.py" "path/to/document.md" "path/to/document.pdf" --theme modern
```

*(If running inside the repository directory, you can also use `python skills/md-pdf/scripts/convert.py ...`)*

### Step 3: Present Dual File Links to the User
Conclude the response with clear, clickable markdown links to both outputs:

```markdown
### 📦 Generated Deliverables
- 📄 **Markdown Document:** [`document.md`](file:///absolute/path/to/document.md)
- 📑 **Publication PDF:** [`document.pdf`](file:///absolute/path/to/document.pdf)
```

---

## 🎨 Available Themes & Styling Options

Pass `--theme <name>` to `convert.py`:

| Theme | Accent Color | Vibe / Recommended Use Case |
| :--- | :--- | :--- |
| **`modern`** *(Default)* | Royal Blue (`#2563eb`) | General technical reports, software documentation, developer guides. |
| **`executive`** | Deep Teal (`#0f766e`) | Board pitches, business plans, grant proposals, management briefings. |
| **`academic`** | Indigo / Slate (`#4338ca`) | Research papers, mathematical summaries, algorithmic analyses. |
| **`minimal`** | Monochrome Dark (`#18181b`) | Minimalist black & white documentation, formal letters, plain audits. |

### Additional CLI Flags

- `--title "Custom Title"`: Override the top banner title.
- `--author "Author Name"`: Set custom author in metadata.
- `--landscape`: Render the PDF in landscape orientation (great for wide comparison tables).
- `--no-header`: Omit the top cover metadata banner.
- `--save-html "path/to/debug.html"`: Save the intermediate rendered HTML file.

---

## 💡 Markdown Formatting Tips for Optimal PDF Output

1. **Page Breaks**: Insert `<!-- pagebreak -->` on its own line wherever a section should start on a fresh page.
2. **Callout Boxes**: Use standard GitHub-style alerts:
   - `> [!NOTE]` $\rightarrow$ Blue informational box.
   - `> [!TIP]` $\rightarrow$ Green recommendation box.
   - `> [!IMPORTANT]` $\rightarrow$ Purple high-priority box.
   - `> [!WARNING]` $\rightarrow$ Amber cautionary box.
   - `> [!CAUTION]` $\rightarrow$ Red critical warning box.
3. **Syntax Highlighting**: Always specify language tags in code fences (e.g. ```` ```python ````, ```` ```typescript ````, ```` ```json ````, ```` ```bash ````).
4. **Tables**: Keep column headers concise. Tables automatically avoid breaking across pages when possible.
