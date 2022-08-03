# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums):
        curr = 0
        for num in nums:
            curr ^= num
        return curr
    def singleNumberCommented(self, nums):
        # start at 0
        curr = 0
        # loop over each number
        for num in nums:
            # compare and update bits in this number using the XOR operator
            curr ^= num
        # return the final result (every duplicate will be cancelled in this process)
        return curr