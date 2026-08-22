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
│   ├── dev-auto/                  <-- Autonomous Pipeline Dispatcher (Auto-selects 2-agent or 3-agent)
│   │   └── SKILL.md
│   ├── triad-auto/                <-- Autonomous Pipeline Dispatcher Alias
│   │   └── SKILL.md
│   ├── triad-dev-tester/          <-- Developer -> Tester 2-Agent Shortcut
│   │   └── SKILL.md
│   ├── triad-dev-auditor/         <-- Developer -> Auditor 2-Agent Shortcut
│   │   └── SKILL.md
│   ├── dev-tester/                <-- Fast Dev + QA Shortcut
│   │   └── SKILL.md
│   ├── dev-auditor/               <-- Fast Dev + Audit Shortcut
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
| **`dev-auto`** / **`triad-auto`** | **Autonomous Pipeline Dispatcher:** Evaluates task requirements (documentation, refactoring, new feature, or critical system) and automatically routes to the optimal 2-agent (`dev-auditor`, `dev-tester`) or 3-agent (`triad`) workflow. | [`skills/dev-auto/SKILL.md`](file:///skills/dev-auto/SKILL.md) |
| **`triad-agent-workflow`** | Universal multi-agent software engineering execution pipeline with configurable modes: **Full Triad** (`Developer -> Tester -> Auditor`, default), **Dev+Tester** (`Developer -> Tester`), or **Dev+Auditor** (`Developer -> Auditor`). | [`skills/triad-agent-workflow/SKILL.md`](file:///skills/triad-agent-workflow/SKILL.md) |
| **`triad-dev-tester`** / **`dev-tester`** | Fast 2-agent pipeline executing **Developer ➔ Tester**. Implements code and runs native test runners to guarantee 100% test coverage. | [`skills/triad-dev-tester/SKILL.md`](file:///skills/triad-dev-tester/SKILL.md) |
| **`triad-dev-auditor`** / **`dev-auditor`** | Fast 2-agent pipeline executing **Developer ➔ Auditor**. Implements/refactors code and runs static analysis, linters, and security quality gating. | [`skills/triad-dev-auditor/SKILL.md`](file:///skills/triad-dev-auditor/SKILL.md) |
| **`md-pdf`** | Authors, formats, and publishes outputs simultaneously as clean GitHub-Flavored Markdown (`.md`) and high-resolution, print-ready PDF (`.pdf`) documents. | [`skills/md-pdf/SKILL.md`](file:///skills/md-pdf/SKILL.md) |
| **`style-extractor`** | Analyzes user-provided writing samples, articles, or documents to extract 6-dimensional stylometric signatures. | [`skills/style-extractor/SKILL.md`](file:///skills/style-extractor/SKILL.md) |
| **`gemini-spark`** | Advanced Playwright automation engine for Google Gemini Spark. | [`skills/gemini-spark/SKILL.md`](file:///skills/gemini-spark/SKILL.md) |

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
