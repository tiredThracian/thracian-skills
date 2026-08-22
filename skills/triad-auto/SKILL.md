---
name: triad-auto
description: >-
  Intelligent Autonomous Triad Coordinator. Analyzes task context and dynamically selects the best pipeline configuration: Dev+Auditor, Dev+Tester, or Full Triad.
---

# Autonomous Triad Pipeline Coordinator (`triad-auto`)

Alias for [`dev-auto`](file:///skills/dev-auto/SKILL.md). Dynamically selects the optimal agent combination based on whether the task is documentation, refactoring, feature implementation, or mission-critical architecture.

## ⚡ Execution Pipeline
```text
[ USER TASK ] ➔ [ 🧠 Heuristic Classifier ] ➔ [ Auto-Selected 2-Agent or 3-Agent Pipeline ] ➔ [ FINAL REPORT ]
```
