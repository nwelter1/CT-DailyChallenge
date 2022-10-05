from typing import List
class Solution:
    # Time O(n) | Space O(n)
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1
        return [1] + digits

    def commented(self, digits):
        # Go from back to front
        i = len(digits) - 1
        # loop over until we reach the first digit
        while i >= 0:
            # if the current digit is a 9, make it a 0
            if digits[i] == 9:
                digits[i] = 0
            # if it's not a 9, just increment it and return -- easy!
            else:
                digits[i] += 1
                return digits
            # keep moving back if we have 9's
            i -= 1
        # in a case where we have all 999's, we need to add a 1. for instance,
        # [9,9,9] becomes [1,0,0,0]
        return [1] + digits

    def tsC(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1 # O(1) Space -- just an int
        while i >= 0: # O(n) Time
            if digits[i] == 9: # Constant
                digits[i] = 0
            else: # Constant
                digits[i] += 1
                return digits
            i -= 1
        return [1] + digits # O(n) Time and O(n) Space creating a new array and making a copy of old one