# O(log10 n) Time | O(1) Space
# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        curr = 0
        while x > curr:
            curr = curr*10 + x % 10
            x //= 10
        return x == curr or x == curr//10
    def commented(self, x: int) -> bool:
        # if x is negative or a number ending in 0, False
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # set up a current number as placeholder to
        # rebuild the integer by grabbing each trailing digit
        # by dividing by 10
        curr = 0
        while x > curr:
            # update curr to reflect the final digit of the original
            # number being added
            # ie. 121 -> curr = (0*10) + (121 % 10) = 1
            # curr = (1*10) +  
            curr = curr*10 + x % 10
            x //= 10
        # if we rebuild x or just need one more step for that to happen, return True
        return x == curr or x == curr//10