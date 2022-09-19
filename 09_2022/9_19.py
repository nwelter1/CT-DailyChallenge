from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr = 0
        for num in nums:
            curr ^= num
        return curr
    def commented(self, nums: List[int]) -> int:
        # set up starting number at 0
        curr = 0
        # loop over nums
        for num in nums:
            # flip the bits in accordance to the bitwise operator. This operation
            # will "flip" any '1' bits that are the same when comparing 2 numbers
            # ie. binary for 1 == 000001. If we come across another 1, here is the comparison:
            # 000001
            # 000001
            # result == 000000 which is '0'
            curr ^= num
        # since we have all duplicates that cancel each other out -- we are left with the single digit
        return curr
