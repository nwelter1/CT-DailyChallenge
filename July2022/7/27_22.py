# https://leetcode.com/problems/count-prefixes-of-a-given-string/submissions/
from typing import List
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            i = 0
            while i < len(word) and i < len(s):
                if word[i] == s[i] and i == len(word)-1:
                    count += 1
                    i += 1
                elif word[i] == s[i]:
                    i += 1
                else:
                    break
        return count
    def countPrefixesOneLiner(self, words: List[str], s: str) -> int:
        return len([w for w in words if w == s[:len(w)]])

