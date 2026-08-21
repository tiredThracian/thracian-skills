# 🏛️ Thracian Skills — Antigravity Agent Skills Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Antigravity Ready](https://img.shields.io/badge/Antigravity-Thracian%20Skills-purple.svg)](https://github.com/tiredThracian/thracian-skills)

**Thracian Skills** is a general-purpose monorepo collection of modular, production-ready agent skills for **Google Antigravity (AGY)** agents. You can install **all skills** at once or select **individual skills** on demand.

---

## 📂 Repository Structure

```text
thracian-skills/
├── skills/
│   ├── gemini-spark/              <-- Gemini Spark Automation Skill
│   │   ├── SKILL.md
│   │   └── scripts/
│   │       ├── index.js
│   │       └── package.json
│   ├── md-pdf/                    <-- Dual Output Markdown & Publication PDF Publisher
│   │   ├── SKILL.md
│   │   └── scripts/
│   │       └── convert.py
│   ├── style-extractor/           <-- Writing Style Extraction & Voice Cloning Skill
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── STYLOMETRIC_RESEARCH_GUIDE.md
│   ├── triad-agent-workflow/      <-- Configurable Multi-Agent Pipeline (Triad, Dev-Tester, Dev-Auditor)
│   │   └── SKILL.md
│   └── [future-skills...]/        <-- Additional skills added over time
├── setup.bat                      <-- Installer (All skills vs Single skill)
├── DEVELOPMENT_REPORT.md
└── README.md
```

---

## 📦 Available Skills

| Skill Name | Description | Path |
| :--- | :--- | :--- |
| **`triad-agent-workflow`** | Universal multi-agent software engineering execution pipeline with configurable modes: **Full Triad** (`Developer -> Tester -> Auditor`, default), **Dev+Tester** (`Developer -> Tester`), or **Dev+Auditor** (`Developer -> Auditor`). Enforces strict role separation across any stack. | [`skills/triad-agent-workflow/SKILL.md`](file:///skills/triad-agent-workflow/SKILL.md) |
| **`md-pdf`** | Authors, formats, and publishes outputs simultaneously as clean GitHub-Flavored Markdown (`.md`) and high-resolution, print-ready PDF (`.pdf`) documents. Features modern typography, Pygments syntax highlighting, responsive tables, GitHub-style callouts (`[!NOTE]`, `[!TIP]`, `[!WARNING]`), custom themes, and automatic page numbering. | [`skills/md-pdf/SKILL.md`](file:///skills/md-pdf/SKILL.md) |
| **`style-extractor`** | Analyzes user-provided writing samples, articles, or documents to extract 6-dimensional stylometric signatures (lexical, syntactic, punctuation, tone, rhetorical, Anti-AI purge matrix). Synthesizes reusable Antigravity Markdown rule files (`.gemini/config/rules/*.md`) or custom skill style guides (`SKILL.md`). | [`skills/style-extractor/SKILL.md`](file:///skills/style-extractor/SKILL.md) |
| **`gemini-spark`** | Advanced Playwright automation engine for Google Gemini Spark (multi-turn context, multi-account support, CDP parallel execution, verbatim responses, batch deletion, workspace file exports). | [`skills/gemini-spark/SKILL.md`](file:///skills/gemini-spark/SKILL.md) |

---

## ⚡ Installation Options

### 1. One-Click Windows Installer (`setup.bat`)

Clone the repository and run `setup.bat`:

```cmd
git clone https://github.com/tiredThracian/thracian-skills.git
cd thracian-skills
```

*   **Install ALL Skills**:
    ```cmd
    setup.bat
    ```
*   **Install a SINGLE Skill (e.g., `md-pdf`, `style-extractor`, or `gemini-spark`)**:
    ```cmd
    setup.bat md-pdf
    setup.bat style-extractor
    setup.bat gemini-spark
    ```
*   **List All Available Skills**:
    ```cmd
    setup.bat list
    ```

---

## 2. Manual / Selective Installation

To install only a specific skill manually, copy its folder from `skills/<skill_name>` to your local Antigravity config directory:

```powershell
# Copy MD-PDF Publisher skill
Copy-Item -Path "skills/md-pdf" -Destination "$env:USERPROFILE\.gemini\config\skills\md-pdf" -Recurse -Force

# Copy Style Extractor skill
Copy-Item -Path "skills/style-extractor" -Destination "$env:USERPROFILE\.gemini\config\skills\style-extractor" -Recurse -Force

# Copy Gemini Spark skill
Copy-Item -Path "skills/gemini-spark" -Destination "$env:USERPROFILE\.gemini\config\skills\gemini-spark" -Recurse -Force
```

---

## ➕ Adding New Skills

To contribute or add a new skill to **Thracian Skills**:
1. Create a new directory under `skills/<your-skill-name>/`.
2. Add a `SKILL.md` file containing instructions and metadata.
3. If helper scripts or Node packages are required, place them inside `skills/<your-skill-name>/scripts/`.
4. Run `setup.bat <your-skill-name>` to verify local deployment.

---

## 📄 License

MIT License. Developed for Google Antigravity Agentic Workflows.
