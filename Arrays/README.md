# Arrays

Solutions to array-based LeetCode problems, grouped here because they share a common toolkit — indexing, iteration, and simple auxiliary structures like hash maps / sets to trade space for time.

## Why this topic first

Arrays are the foundational data structure for almost every other topic in this roadmap. Strong array intuition (indexing, bounds, in-place operations, pair-finding, prefix sums, two pointers on a linear structure) directly feeds into Strings, Hashing, Two Pointers, Sliding Window, and Sorting-based problems.

## Recurring patterns seen in this folder

_(this section grows as more problems are added)_

- **Pair with target sum** — for each element, either scan the rest (O(n²) brute force) or use a hash map of "already seen" values to look up the complement in O(1) (O(n) optimal). Seen in: `001_two_sum.py`.

## Problems solved

| LC # | Title | Difficulty | Pattern | File |
|---|---|---|---|---|
| 1 | Two Sum | Easy | Brute-force pair scan (hash-map optimization pending) | [001_two_sum.py](001_two_sum.py) |

## Standard checklist for every solution in this folder

1. Understand the problem in my own words; note the constraints (size, value range, duplicates allowed?).
2. State a brute-force approach and its time/space complexity.
3. Attempt an optimized approach; use hints only if stuck.
4. Implement in Python — clean names, small helpers where useful.
5. Run through: normal case, empty / minimum-size input (where valid), duplicates, largest allowed input.
6. Re-analyze final time and space complexity honestly.
7. Add the file header (problem, link, approach summary, complexity).
8. Commit with a meaningful message describing what was solved and how.

## Notes for future problems in this folder

- If two-pointer or sliding-window approaches start to appear, factor those out into their own topic folders instead of duplicating here.
- If a problem is fundamentally about hashing rather than the array itself, it belongs in `Hashing/`, not `Arrays/`.
