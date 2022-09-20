from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return -1
    def commented(self, nums: List[int], target: int) -> int:
        # establish bounds of your list idxs
        left = 0
        right = len(nums) - 1
        # while we still have numbers to look at...
        while left <= right:
            # find a mid point
            mid = (left + right) // 2
            # if that midpoint holds the target, we're done
            if nums[mid] == target:
                return mid
            # if it is greater than the target, ignore the right half
            if target < nums[mid]:
                right = mid - 1
            # less than target, ignore the left half
            elif target > nums[mid]:
                left = mid + 1
        # if we never find it, return -1
        return -1