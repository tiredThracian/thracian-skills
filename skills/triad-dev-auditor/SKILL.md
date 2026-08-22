---
name: triad-dev-auditor
description: >-
  Developer -> Auditor 2-agent software engineering pipeline. Invokes the Developer subagent to write/refactor code, followed immediately by the Auditor subagent for static analysis, linters, design token checks, and security quality gating.
---

# Triad: Developer + Auditor Mode (`triad-dev-auditor`)

This skill executes the **Developer ➔ Auditor** 2-agent subset of the `triad-agent-workflow`.

## ⚡ Execution Pipeline
```text
[ USER TASK ] ➔ [ 1. DEVELOPER (Feature & Refactor) ] ➔ [ 2. AUDITOR (Linter & Quality Gate) ] ➔ [ FINAL REPORT ]
```

## 🤖 Workflow Instructions
1. **Developer Phase:** Spawn `Developer Subagent` to implement/refactor code cleanly according to project architecture.
2. **Auditor Phase:** Spawn `Auditor Subagent` to run linters, static analyzers, and security checks. Generate a formal PASS/FAIL quality report.
3. **Delivery:** Summarize the implementation and present the audit findings. (Unit test writing phase is skipped).
