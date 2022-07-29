# https://leetcode.com/problems/isomorphic-strings/submissions/
class Solution:
    def isIsomorphic(self, s, t):
        sd, td = {}, {}
        for i in range(len(s)):
            if s[i] in sd and sd[s[i]] != t[i]:
                return False
            if t[i] in td and td[t[i]] != s[i]:
                return False
            sd[s[i]] = t[i]
            td[t[i]] = s[i]
        return True