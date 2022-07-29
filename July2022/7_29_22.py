# https://leetcode.com/problems/isomorphic-strings/submissions/
# https://leetcode.com/problems/isomorphic-strings/
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
	# commented version
    def isIsomorphicCommented(self, s, t):
		# create 2 dicts for character mapping 
        sd, td = {}, {}
		# loop over s (t is same len so we can loop over both at same time)
        for i in range(len(s)):
			# if the first character is in first dict and its mapping is
			# not the current char in t, this is False, we have a mismatch
            if s[i] in sd and sd[s[i]] != t[i]:
                return False
			# same thing for other side
            if t[i] in td and td[t[i]] != s[i]:
                return False
			# if we do not return False
			# add mappings into each dict
            sd[s[i]] = t[i]
            td[t[i]] = s[i]
		# if we make it all the way through with no False returns
        return True