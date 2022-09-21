# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# O(n*m) Time O(m) Space where n == len haystack and m == len needle
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        wLen = len(needle)
        for i in range(len(haystack)):
            print(haystack[i:i+wLen])
            if haystack[i:i+wLen] == needle:
                return i
        return -1