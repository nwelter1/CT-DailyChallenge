# https://leetcode.com/problems/palindrome-permutation/submissions/
# O(n) Time | O(n) Space
def canPermutePalindrome(s):
	odds = 0
	counts = {}
	for char in s:
		counts[char] = counts.get(char,0) + 1
		if counts[char] % 2:
			odds += 1
		else:
			odds -= 1
	return odds < 2

# Commented
def canPermutePalindrome(s):
	# count total odd occurances
	odds = 0
	# dict for counter
	counts = {}
	# loop over list to get freq of each char
	for char in s:
		counts[char] = counts.get(char,0) + 1
		# if the current count is odd, add 1 to odd counter
		if counts[char] % 2:
			odds += 1
		# if current count is now even, subtract 1 from odd counter
		else:
			odds -= 1
	# return True if odd count < 2, False if not
	return odds < 2