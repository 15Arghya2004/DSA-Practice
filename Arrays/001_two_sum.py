"""
LeetCode #1 - Two Sum
Difficulty: Easy
Topic: Arrays (+ Hashing)
Link: https://leetcode.com/problems/two-sum/

------------------------------------------------------------
PROBLEM STATEMENT
------------------------------------------------------------
Given an array of integers `nums` and an integer `target`, return the
indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you
may not use the same element twice. You can return the answer in any
order.

Constraints:
    2 <= len(nums) <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target  <= 10^9
    Only one valid answer exists.

Examples:
    nums = [2, 7, 11, 15], target = 9   ->  [0, 1]
    nums = [3, 2, 4],      target = 6   ->  [1, 2]
    nums = [3, 3],         target = 6   ->  [0, 1]

------------------------------------------------------------
APPROACH USED (Brute Force)
------------------------------------------------------------
For every index `i`, scan every later index `j` (j > i) and check if
nums[i] + nums[j] == target. Using j = i+1 avoids re-checking pairs and
prevents using the same element twice.

Time complexity : O(n^2)   -- nested loops over the array.
Space complexity: O(1)     -- only a couple of loop variables.

Accepted on LeetCode (all 3 example cases passed, runtime 0 ms on the
sample input). Works within the given constraint (n <= 10^4 -> up to
~10^8 checks in the worst case, borderline but acceptable here).
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype: list[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# ------------------------------------------------------------
# FOLLOW-UP / OPTIMIZATION (to be implemented in a later session)
# ------------------------------------------------------------
# The brute force above is O(n^2). The standard optimization is a
# single-pass hash map:
#
#   - Walk the array once.
#   - For each element x at index i, compute complement = target - x.
#   - If complement is already in the map, we found the answer.
#   - Otherwise, store x -> i in the map and continue.
#
# This trades O(n) extra space for O(n) time on average.
#
# TODO: implement `twoSumHashMap` myself in the next revision.
#
# def twoSumHashMap(self, nums, target):
#     seen = {}
#     for i, x in enumerate(nums):
#         # complement = target - x
#         # if complement in seen: return [seen[complement], i]
#         # seen[x] = i
#         pass
# ------------------------------------------------------------


if __name__ == "__main__":
    # Quick local sanity checks (not part of the LeetCode submission).
    sol = Solution()
    assert sorted(sol.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(sol.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(sol.twoSum([3, 3], 6)) == [0, 1]
    print("All sample cases passed.")
