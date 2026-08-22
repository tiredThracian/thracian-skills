---
name: dev-auto
description: >-
  Intelligent Autonomous Multi-Agent Coordinator. Analyzes the incoming task type and automatically selects the optimal execution pipeline: Dev+Auditor (for docs, specs, refactors, security), Dev+Tester (for fast feature/bugfix QA), or Full Triad (for critical production code, full-stack features).
---

# Autonomous Pipeline Coordinator (`dev-auto` / `triad-auto`)

This skill acts as an **intelligent dispatcher** that analyzes the user's task characteristics and automatically selects and executes the most appropriate subagent pipeline without requiring manual mode configuration.

---

## 🧠 Decision Engine & Heuristics Matrix

When `dev-auto` is triggered, the coordinator evaluates the task against the following matrix:

| Task Type & Signature | Auto-Selected Mode | Pipeline Flow | Rationale |
| :--- | :--- | :--- | :--- |
| **Documentation, Specs, PRDs, Guides, Reports, Rule Files** | **`dev-auditor`** | `Developer ➔ Auditor` | Non-executable text artifacts do not need unit test runners; they require editorial review, consistency, and style auditing. |
| **Refactoring, Linter Fixes, Style Migrations, Security Hardening** | **`dev-auditor`** | `Developer ➔ Auditor` | Structural cleanup and static compliance require strict linter and security gatekeeping over new test suites. |
| **New Features, Algorithms, Bug Fixes, Data Parsers (Standard)** | **`dev-tester`** | `Developer ➔ Tester` | Executable code requiring dynamic verification, unit tests, and 100% test pass guarantee. |
| **Critical Core Modules, Multi-Layer Architecture, Full Releases** | **`triad` (Full Triad)** | `Developer ➔ Tester ➔ Auditor` | High-stakes production components demanding both 100% test pass verification AND strict security/linter quality gating. |

---

## ⚡ Execution Workflow

1. **Task Analysis Phase:**
   - Detect task nature: Code vs. Documentation vs. Architecture vs. Refactoring.
   - Announce the selected strategy to the user with a brief rationale:
     > *"🧠 `dev-auto` Stratejisi: Bu görev bir [Dokümantasyon / Kod Geliştirme / Refactor] işi olduğu için `[dev-auditor / dev-tester / Full Triad]` hattı seçildi."*

2. **Autonomous Execution:**
   - **Phase 1 (Developer):** Implement or author the requested files.
   - **Phase 2 (Tester or Auditor):** Run the corresponding QA test runner or static analysis / audit.
   - **Phase 3 (If Full Triad):** Run the third agent for complete quality gating.

3. **Final Delivery:**
   - Present the deliverables, test metrics, and/or audit reports clearly.
