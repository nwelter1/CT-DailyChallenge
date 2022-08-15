# https://leetcode.com/problems/power-of-two/
# Time: O(log n) | Space: O(1)
class Solution:
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1
    def isPowerOfTwoCommented(self, n):
        # base case, if 0, cannot be a power of 2
        if n == 0:
            return False
        # keep dividing n by 2 if it is an even number after division
        # ie. if we could divide by 2, this could be a power of 2
        while n % 2 == 0:
            n /= 2
        # eventually, n will no longer be even if we divide by 2
        # in this case, the only acceptable odd number is 1
        # ie. 1*2*2*2*2*2 is a valid product for a power of 2
        # same could be said going reverse, which is what we are doing
        # 16/2/2/2/2 == 1 so 16 is a power of 2
        # 14/2 == 7 which is odd and != 1, so this is False
        return n == 1

