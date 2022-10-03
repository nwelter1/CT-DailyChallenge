# O(n+m) Time | O(n) Space where n == len(jewels) & m == len(stones)
# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        s = set(jewels)
        for stone in stones:
            if stone in s:
                counter += 1
        return counter
    def commented(self, jewels: str, stones: str) -> int:
        # counter for final amount of jewels
        counter = 0
        # create set of jewels for constant time lookup
        s = set(jewels)
        # loop over each stone
        for stone in stones:
            # check to see if it is a jewel
            if stone in s:
                # if so, increase counter
                counter += 1
        # return final jewel count
        return counter
    def commentedTimeSpace(self, jewels: str, stones: str) -> int: # calling n == len(jewels), m == len(stones)
        counter = 0 # O(1) Time and Space
        s = set(jewels) # O(n) Time to loop over jewels to create the set and O(n) Space to store the set in memory
        for stone in stones: # O(m) Time to loop over stones
            if stone in s: # O(1) Time membership check for set
                counter += 1 # O(1) Time/Space math operation
        return counter