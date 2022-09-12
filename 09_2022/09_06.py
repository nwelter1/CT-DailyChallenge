# O(n) Time O(1) Space
# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum