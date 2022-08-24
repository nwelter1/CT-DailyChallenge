# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List
# O(n) Time | O(1) Space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l, r]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -=1

    def commented(self, numbers: List[int], target: int) -> List[int]:
        # left and right pointers at beginning and end
        l = 0
        r = len(numbers) - 1
        # adjust left and right until they meet at a midpoint
        while l < r:
            # if the numbers sum to target, we found the answer!
            if numbers[l] + numbers[r] == target:
                return [l, r]
            # if the sum is less than the target, the only way to inscrease
            # is by moving the left pointer toward the middle (list is in asc order)
            elif numbers[l] + numbers[r] < target:
                l += 1
            # if the sum is too big, the only way toward target is down
            # move the right pointer toward the middle
            else:
                r -=1
            # repeat the process until we get to our solution