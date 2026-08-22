---
name: dev-auditor
description: >-
  Fast Developer -> Auditor 2-agent engineering workflow. Implements/refactors code and immediately audits it for linters, design conventions, and security quality gating.
---

# Dev + Auditor Pipeline (`dev-auditor`)

Shortcut alias for the `Developer ➔ Auditor` 2-agent engineering workflow.

## ⚡ Execution Pipeline
```text
[ USER TASK ] ➔ [ 1. DEVELOPER ] ➔ [ 2. AUDITOR ] ➔ [ FINAL REPORT ]
```

## 🤖 Workflow Instructions
1. **Developer Phase:** Implement or refactor code according to architecture and project rules.
2. **Auditor Phase:** Run static analysis, linters, and security checks. Deliver PASS/FAIL Audit Grade.
3. **Delivery:** Report files modified and audit findings.
