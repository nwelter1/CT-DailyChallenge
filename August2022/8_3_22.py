from typing import List
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3:
            return len(s)
        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        d = {}

        max_len = 2

        while right < len(s):
            # when the slidewindow contains less than 3 characters
            d[s[right]] = right
            right += 1

            # slidewindow contains 3 characters
            if len(d) == 3:
                # delete the leftmost character
                del_idx = min(d.values())
                del d[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len


# https://leetcode.com/problems/binary-search/solution/
class Solution2:
    def binarySearch(self, nums: List[int], target: int) -> int:
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

    def binarySearchCommented(self, nums: List[int], target: int) -> int:
        # start left and right pointers at beginning and end of list
        left = 0
        right = len(nums) - 1
        # loop until we pass the middle
        while left <= right:
            # find mid point between left and right
            mid = (left + right) // 2
            # if this midpoint is == target, return the index
            if nums[mid] == target:
                return mid
            # if the midpoint > target move the right pointer
            # so we are only looking at left half of list
            if target < nums[mid]:
                right = mid - 1
            # if the midpoint < target move the left pointer
            # so we are only looking at right half of list
            elif target > nums[mid]:
                left = mid + 1
        # if we never find a midpoint == target, return -1
        return -1