# https://leetcode.com/problems/first-unique-character-in-a-string/
def firstUniqChar(s):
	res = {}
	for char in s:
		res[char] = res.get(char, 0) + 1
	for i in range(len(s)):
		if res[s[i]] == 1:
			return i
	return -1

# Commented Version
def firstUniqChar(s):
	# create empty dict to count freq of letters
	res = {}
	# fill the dict with frequency of each letter
	for char in s:
		res[char] = res.get(char, 0) + 1
	# loop over original string
	for i in range(len(s)):
		# first letter with a count of 1, return the idx
		if res[s[i]] == 1:
			return i
	# if we found no unique letters, return -1
	return -1