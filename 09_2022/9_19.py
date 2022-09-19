from typing import List
# https://leetcode.com/problems/single-number/
class Solution:
    # O(n) Time | O(1) Space
    def singleNumberBitWise(self, nums: List[int]) -> int:
        curr = 0
        for num in nums:
            curr ^= num
        return curr
    def bitwiseCommented(self, nums: List[int]) -> int:
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
    # O(n) Time | O(n) Space
    def singleNumberSet(self, nums: List[int]) -> int:
        curr = 0
        seen = set()
        for num in nums:
            if num in seen:
                curr -= num
            else:
                curr += num
                seen.add(num)
        return curr
    def setCommented(self, nums: List[int]) -> int:
        # establish counter for answer
        curr = 0
        # create empty set to track what we have seen with O(1) Time
        seen = set()
        # loop over nums
        for num in nums:
            # if we have seen this number, this is a dupe
            # subtract it from the counter
            if num in seen:
                curr -= num
            # if not, we will add to the set and add the number to the counter
            else:
                curr += num
                seen.add(num)
        # we'll be left with all nums cancelled out aside from the non-dupe
        return curr

print(
Solution().singleNumberSet([2,2,1,1,3]))

    
