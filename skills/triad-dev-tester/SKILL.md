---
name: triad-dev-tester
description: >-
  Developer -> Tester 2-agent software engineering pipeline. Invokes the Developer subagent to write/implement code, followed immediately by the Tester subagent to write unit/integration tests and verify 100% test pass rate.
---

# Triad: Developer + Tester Mode (`triad-dev-tester`)

This skill executes the **Developer ➔ Tester** 2-agent subset of the `triad-agent-workflow`.

## ⚡ Execution Pipeline
```text
[ USER TASK ] ➔ [ 1. DEVELOPER (Feature & Code) ] ➔ [ 2. TESTER (QA & Tests) ] ➔ [ FINAL REPORT ]
```

## 🤖 Workflow Instructions
1. **Developer Phase:** Spawn `Developer Subagent` to implement the feature/bugfix cleanly without placeholders.
2. **Tester Phase:** Spawn `Tester Subagent` to write comprehensive unit/integration tests and run the native test runner until all tests pass.
3. **Delivery:** Summarize the code changes and test execution results for the user. (Formal auditor phase is skipped).
