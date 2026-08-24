"""
LeetCode #15 - 3Sum
Difficulty: Medium
Topic: Two Pointers (on sorted array) + Duplicate Handling
Link: https://leetcode.com/problems/3sum/

------------------------------------------------------------
PROBLEM STATEMENT
------------------------------------------------------------
Given an integer array `nums`, return ALL triplets [nums[i], nums[j], nums[k]]
such that:
    i != j, i != k, j != k, and
    nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.

Constraints:
    3 <= len(nums) <= 3000
    -10^5 <= nums[i] <= 10^5

Examples:
    nums = [-1, 0, 1, 2, -1, -4]  ->  [[-1, -1, 2], [-1, 0, 1]]
    nums = [0, 1, 1]              ->  []
    nums = [0, 0, 0]              ->  [[0, 0, 0]]

------------------------------------------------------------
APPROACH: Sort + Two Pointers
------------------------------------------------------------
1. Sort the array. Sorting unlocks two things:
     (a) Duplicate skipping becomes trivial — equal elements sit next to
         each other, so we can skip them by comparing to the previous
         index instead of using a set.
     (b) Two pointers work on a sorted range — moving `left` right
         increases the sum, moving `right` left decreases the sum. That
         makes the inner search O(n) instead of O(n^2).

2. Fix one element with the outer loop (index i). Then for the remaining
   subarray to the right of i, run a classic two-pointer search for a pair
   whose sum equals -nums[i].

3. Early break: once nums[i] > 0, all three numbers would be positive
   (array is sorted), so their sum can never be zero. Stop the outer loop.

4. Duplicate handling — three places matter:
     - Outer loop: if nums[i] == nums[i-1], skip. Otherwise we would
       generate the same triplet with a different i.
     - After finding a valid triplet: advance `left` past any equal
       neighbors, and `right` past any equal neighbors. Otherwise the same
       triplet would be recorded again.

Time complexity : O(n^2)
    - Sorting: O(n log n)
    - Outer loop: O(n), inner two-pointer sweep: O(n) -> O(n^2)
    - The n^2 term dominates.

Space complexity: O(1) extra (ignoring the output list and Python's
    internal sort auxiliary space).

------------------------------------------------------------
LEARNING NOTES
------------------------------------------------------------
- Concept understood from a walkthrough with Gemini; implementation written
  from scratch, not copy-pasted.
- Ownership follow-up: solve a related pattern problem WITHOUT any external
  help to confirm mastery. Candidates: "Two Sum II - Input Array Is Sorted"
  (LC #167), "3Sum Closest" (LC #16), or "4Sum" (LC #18).
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()  # Step 1: Sort the array (O(N log N))
        for i in range(len(nums) - 2):
            # Optimization: Agar pehla number hi > 0 hai, toh 3 positive numbers ka sum kabhi 0 nahi ho sakta
            if nums[i] > 0:
                break
            # Duplicate Skip #1: Agar current element previous wale jaisa hai, toh skip karo
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Step 2: Two Pointers setup
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1  # Sum chhota hai, badhaane ke liye left aage badhao
                elif total > 0:
                    right -= 1  # Sum bada hai, ghataane ke liye right peeche lao
                else:
                    # Target 0 mil gaya
                    res.append([nums[i], nums[left], nums[right]])
                    # Pointer move karo
                    left += 1
                    right -= 1
                    # Duplicate Skip #2: Same left value dobara na aaye
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Duplicate Skip #3: Same right value dobara na aaye
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res


if __name__ == "__main__":
    # Quick local sanity checks (not part of the LeetCode submission).
    def _norm(triplets):
        return sorted(sorted(t) for t in triplets)

    sol = Solution()
    assert _norm(sol.threeSum([-1, 0, 1, 2, -1, -4])) == _norm([[-1, -1, 2], [-1, 0, 1]])
    assert _norm(sol.threeSum([0, 1, 1])) == []
    assert _norm(sol.threeSum([0, 0, 0])) == [[0, 0, 0]]
    assert _norm(sol.threeSum([-2, 0, 0, 0, 2])) == [[-2, 0, 2]]  # duplicate-skip stress
    print("All sample cases passed.")
