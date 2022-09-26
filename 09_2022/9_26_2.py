from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.findLower(nums, target)
        if lower_bound == -1:
            return [-1,-1]
        upper_bound = self.findUpper(nums, target)
        return [lower_bound, upper_bound]
    def findLower(self, nums, target):
        n = len(nums)
        start, end = 0, n-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                if mid == start or nums[mid-1] < target:
                    return mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    def findUpper(self, nums, target):
        n = len(nums)
        start, end = 0, n-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                if mid == end or nums[mid+1] > target:
                    return mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

print(Solution().searchRange([0,1,1,2,3,4,5], 3))
