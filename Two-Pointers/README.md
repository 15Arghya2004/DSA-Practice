# Two Pointers

Solutions to problems whose core pattern is running two indices (usually one from each end, or one slow + one fast) across an array — often after sorting.

## Why this pattern

Two pointers replaces a nested loop with a linear sweep by using **structure** (usually sortedness) to decide which pointer to move. Wherever you'd write "for every pair", ask first: "is the input sorted, or can I sort it? If yes, can I use directional moves to prune?"

## Recurring patterns seen in this folder

- **Sorted array + opposite-end pointers** — start `left = 0`, `right = n-1`. Compare current pair's aggregate to a target: move `left` right if too small, move `right` left if too big. Seen in: `015_3sum.py` (nested inside an outer fix-one-element loop).
- **Duplicate skipping in a sorted array** — after finding a valid answer or moving past an element, advance a pointer while it equals its predecessor. Cheap because equal values sit adjacent after sorting.

## Problems solved

| LC # | Title | Difficulty | Pattern | File |
|---|---|---|---|---|
| 15 | 3Sum | Medium | Sort + two pointers + duplicate skip | [015_three_sum.py](015_three_sum.py) |

## Standard checklist for every solution in this folder

1. Understand the problem in my own words; note the constraints (size, value range, duplicates allowed?).
2. Ask: is the input sorted or can I sort it? What does sorting unlock?
3. Decide pointer setup (opposite ends? slow/fast?) and the move rule.
4. Handle duplicates explicitly if the problem forbids duplicate answers.
5. Implement in Python — clean names, small helpers where useful.
6. Test: normal case, all-same-values, empty / minimum size (where valid), max size.
7. Analyze time and space complexity honestly.
8. Commit with a meaningful message describing what was solved and how.

## Notes for future problems in this folder

- If a problem is purely "find a pair with sum X" on an unsorted array with no need to return indices in original order, hashing (`Hashing/`) may be faster to implement than sort + two pointers. Choose based on constraints and what the output requires.
- Sliding-window problems are a *specialization* of two pointers where both pointers move in the same direction and maintain a window invariant. Those live in `Sliding-Window/`, not here.
