---
name: triad-agent-workflow
description: >-
  Universal multi-agent software engineering execution pipeline with configurable modes: Full Triad (Developer -> Tester -> Auditor by default), Dev+Tester (Developer -> Tester), or Dev+Auditor (Developer -> Auditor).
  Use whenever a coding feature, refactor, bugfix, or architectural task should be executed with strict role separation across development, testing, and auditing.
---

# Triad Agent Workflow (Multi-Agent Engineering Pipeline)

This skill provides a **project-agnostic, universal engineering workflow** that enforces clean separation of concerns using specialized subagents:
1. **Developer (Coder Agent):** Implements production code, models, architecture, and contracts.
2. **Tester (QA & Test Agent):** Writes unit/integration tests, edge cases, and verifies 100% test execution.
3. **Auditor (Reviewer & Quality Gate Agent):** Audits linters, design tokens/style rules, security, contracts, and regression parities.

---

## 🎛️ Execution Modes (Çalışma Modları)

The pipeline automatically adapts based on user intent, defaulting to the full 3-agent triad if no specific mode is specified:

| Mode | Pipeline Flow | When to Use / Triggers |
| :--- | :--- | :--- |
| **`triad` / Full** *(Default)* | `Developer ➔ Tester ➔ Auditor` | Production features, critical refactors, default triad requests. |
| **`dev-tester`** | `Developer ➔ Tester` | Fast feature/bugfix development with test verification, skipping formal audit. Triggered by *"dev + tester"*, *"sadece test yaz"*, *"auditor istemiyorum"*, `--mode dev-tester`. |
| **`dev-auditor`** | `Developer ➔ Auditor` | Refactoring, styling, security fixes, or contract updates without writing new unit tests. Triggered by *"dev + auditor"*, *"tester istemiyorum"*, *"sadece denetle/audit et"*, `--mode dev-auditor`. |
| **`audit-only` / `qa-only`** | `Tester` or `Auditor` | Running QA or audit on existing code without developer phase. |

---

## ⚡ Execution Pipeline Schemas

### 1. Default: Full Triad Mode (`Developer ➔ Tester ➔ Auditor`)
```text
[ USER TASK ]
      │
      ▼
┌────────────────────────────────────────────────────────┐
│ PHASE 1: DEVELOPER SUBAGENT (Coder)                    │
│ - Reads project rules, contracts, and architecture.    │
│ - Implements production code cleanly & modularly.      │
└──────────────────────────┬─────────────────────────────┘
                           │ (Implementation Complete)
                           ▼
┌────────────────────────────────────────────────────────┐
│ PHASE 2: TESTER SUBAGENT (QA & Verification)           │
│ - Inspects diffs & writes unit/integration/edge tests. │
│ - Runs project native test runner (100% pass rate).    │
└──────────────────────────┬─────────────────────────────┘
                           │ (All Tests Passing)
                           ▼
┌────────────────────────────────────────────────────────┐
│ PHASE 3: AUDITOR SUBAGENT (Reviewer & Gatekeeper)      │
│ - Runs static analysis, linters & security checks.     │
│ - Audits design tokens / style guide compliance.       │
│ - Issues formal PASS / REJECT Audit Report.            │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
             [ FINAL DELIVERABLE & REPORT ]
```

### 2. Dev + Tester Mode (`Developer ➔ Tester`)
```text
[ USER TASK ] ➔ [ 1. DEVELOPER ] ➔ [ 2. TESTER (QA Runner) ] ➔ [ FINAL REPORT ]
```

### 3. Dev + Auditor Mode (`Developer ➔ Auditor`)
```text
[ USER TASK ] ➔ [ 1. DEVELOPER ] ➔ [ 2. AUDITOR (Quality Gate) ] ➔ [ FINAL REPORT ]
```

---

## 🤖 Standard Subagent Definitions & Roles

### 1. Developer Subagent (`define_subagent` ➔ `invoke_subagent`)
* **Role:** `Feature Developer`
* **Tools:** `enable_write_tools: true`
* **System Prompt Core:**
  - Read project rules, architecture patterns, and conventions.
  - Implement complete production code without placeholders, stubs, or TODOs.
  - Report exact files modified and concise technical rationale.

### 2. Tester Subagent (`define_subagent` ➔ `invoke_subagent`)
* **Role:** `QA & Test Engineer`
* **Tools:** `enable_write_tools: true`
* **System Prompt Core:**
  - Inspect Developer changes and identify edge cases and boundary conditions.
  - Write comprehensive tests matching project test framework (e.g. `pytest`, `npm test`, `cargo test`, `flutter test`).
  - Run the native test runner. Diagnose and resolve failing tests until 100% pass.

### 3. Auditor Subagent (`define_subagent` ➔ `invoke_subagent`)
* **Role:** `Quality & Security Auditor`
* **Tools:** `enable_write_tools: true`
* **System Prompt Core:**
  - Run static analysis and linters (e.g. `ruff`, `eslint`, `clippy`, `flutter analyze`).
  - Verify security, contracts, error handling, and design token compliance.
  - Issue a structured PASS/FAIL Audit Report with clear grading.

---

## 📋 Best Practices for the Parent Coordinator Agent

1. **Mode Detection:** Check if the user requested a specific pairing (`dev-tester`, `dev-auditor`, or full `triad`). Default to full `triad`.
2. **Sequential Handoff:** Pass the output and modified file paths of the previous subagent to the next subagent's prompt context.
3. **Reactive Wakeup:** Do not poll in a loop. Antigravity automatically wakes up the coordinator when a subagent finishes.
4. **Final Summary:** Deliver a clear, consolidated report highlighting files changed, tests verified, and audit results.