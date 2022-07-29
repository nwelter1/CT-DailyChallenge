# https://leetcode.com/problems/isomorphic-strings/submissions/
class Solution:
    def isIsomorphic(self, s, t):
        sd, td = {}, {}
        for i in range(len(s)):
            curr = s[i]
            if s[i] in sd:
                if s[i] != td[sd[s[i]]] or t[i] not in td:
                    return False
            else:
                sd[s[i]] = t[i]
                td[t[i]] = s[i]
        return True