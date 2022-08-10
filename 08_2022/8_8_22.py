# https://leetcode.com/problems/largest-unique-number/

from typing import List
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        big = float('-Inf')
        smallest = None
        for k in d:
            if d[k] == 1 and k > big:
                big = k
                smallest = 1
        return big if smallest else -1