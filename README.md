# DSA-Practice

Structured LeetCode DSA practice focused on problem solving, algorithmic patterns, complexity analysis, and consistent Git-based learning.

---

## 1. Project Overview

This repository is a long-term, structured log of my Data Structures and Algorithms practice. It is not a collection of copy-pasted LeetCode answers. Every solution committed here is one I have understood, implemented, tested, and reviewed myself.

The repository is organized by algorithmic topic so that patterns — not isolated problems — become the unit of learning.

## 2. Objectives

- Build a strong, transferable foundation in DSA.
- Learn to recognize algorithmic patterns across problem variants.
- Practice clean, readable, well-commented code.
- Maintain honest, meaningful commit history that reflects real learning progress.
- Develop the habit of complexity analysis for every solution.

## 3. Learning Philosophy

- Understand before implementing.
- Attempt before asking for hints.
- Own every line of code committed.
- Prefer depth of understanding over volume of problems solved.
- Revisit weak topics rather than rushing forward.

## 4. Problem Source

Primary source: [LeetCode](https://leetcode.com/).
Problems are selected to reinforce a specific pattern or concept rather than at random.

## 5. Topic Roadmap

| # | Topic | Status |
|---|---|---|
| 1 | Arrays | In Progress |
| 2 | Strings | Planned |
| 3 | Hashing / Hash Maps / Sets | Planned |
| 4 | Two Pointers | Planned |
| 5 | Sliding Window | Planned |
| 6 | Binary Search | Planned |
| 7 | Stack | Planned |
| 8 | Queue | Planned |
| 9 | Linked List | Planned |
| 10 | Recursion / Backtracking | Planned |
| 11 | Trees / BST | Planned |
| 12 | Heap / Priority Queue | Planned |
| 13 | Graphs | Planned |
| 14 | Greedy | Planned |
| 15 | Dynamic Programming | Planned |

Statuses are updated only when actual progress is made in a topic.

## 6. Repository Structure

```
DSA-Practice/
├── README.md
├── .gitignore
├── Arrays/
├── Strings/
├── Hashing/
├── Two-Pointers/
├── Sliding-Window/
├── Binary-Search/
├── Stack/
├── Queue/
├── Linked-List/
├── Recursion/
├── Trees/
├── Heap/
├── Graphs/
├── Greedy/
└── Dynamic-Programming/
```

Topic directories are created on demand. A directory appears in the tracked repository only once it contains at least one solution.

## 7. Solution File Naming

Solutions follow a consistent convention:

```
<Topic>/<problem_number>_<snake_case_name>.<ext>
```

Examples:

```
Arrays/001_two_sum.py
Hashing/049_group_anagrams.py
Sliding-Window/003_longest_substring_without_repeating_characters.py
```

Each solution file should contain, at minimum:

- Problem number and title (as a header comment).
- Link to the LeetCode problem.
- Brief approach summary.
- Time and space complexity.
- Clean, tested implementation.

## 8. Problem-Solving Workflow

For every problem:

1. Read and restate the problem in my own words.
2. Identify constraints and edge cases.
3. Attempt a brute-force approach and analyze its complexity.
4. Try to derive an optimized approach; use progressive hints only if stuck.
5. Implement the solution myself.
6. Test against normal, edge, and boundary cases.
7. Analyze final time and space complexity.
8. Commit with a meaningful message and push.

## 9. Difficulty Progression

- **Easy** — used to lock in fundamentals of a new topic.
- **Medium** — the primary difficulty once fundamentals are solid.
- **Hard** — introduced only after consistent success at Medium within the same pattern.

Difficulty is not rushed. A topic is not "done" until multiple variants of its core pattern are handled comfortably.

## 10. Coding Standards

- Clear variable names — no single letters unless idiomatic (e.g., `i`, `j`, `l`, `r`).
- Small, focused functions.
- Comments only where they add real value (approach, invariants, non-obvious steps).
- No dead code, no commented-out experiments.
- Consistent formatting per language conventions.

## 11. Git / GitHub Workflow

Intended flow for each problem:

```
select problem
   → understand problem
   → attempt solution
   → use hints if necessary
   → implement personally
   → test
   → review complexity
   → commit
   → push
```

**Commit message style**

Meaningful, imperative, describes the completed problem and pattern.

Good examples:

```
Solve Two Sum using Hash Map
Solve Longest Substring Without Repeating Characters using Sliding Window
Add iterative in-order traversal for Binary Tree
```

Avoid:

```
update
changes
fix
test
wip
```

One commit per completed, tested problem is the default. Larger refactors get their own commits.

## 12. Progress Tracking

Progress is tracked through:

- The topic roadmap table in this README (updated as topics move from Planned → In Progress → Solid).
- Commit history (which reflects actual, ordered progress).
- Per-topic file counts and the range of problems covered.

I do not overstate progress. A topic is marked further along only when the underlying pattern is actually understood, not merely when a problem in it has been solved.

## 13. Future Scope

- Add short pattern-summary notes per topic once enough problems are solved in it.
- Add revision notes for commonly forgotten patterns.
- Extend to system design and language-specific deep dives once core DSA is solid.
- Optionally publish selected write-ups as blog posts.

---

_Maintained by [Arghya Mahajan](https://github.com/15Arghya2004)._
