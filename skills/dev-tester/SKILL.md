---
name: dev-tester
description: >-
  Fast Developer -> Tester 2-agent engineering workflow. Implements feature/bugfix and immediately writes and runs tests to guarantee 100% pass rate.
---

# Dev + Tester Pipeline (`dev-tester`)

Shortcut alias for the `Developer ➔ Tester` 2-agent engineering workflow.

## ⚡ Execution Pipeline
```text
[ USER TASK ] ➔ [ 1. DEVELOPER ] ➔ [ 2. TESTER ] ➔ [ FINAL REPORT ]
```

## 🤖 Workflow Instructions
1. **Developer Phase:** Implement the code/feature cleanly and modularly.
2. **Tester Phase:** Write unit/integration tests, run the test runner, and verify 100% pass rate.
3. **Delivery:** Report files created/updated and test results.
