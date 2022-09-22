# https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution:
    # O(n) Time | O(n) Space
    def builtInWay(self, s):
        list_s = s.split(" ")
        list_s_reversed = [word[::-1] for word in list_s]
        return ' '.join(list_s_reversed)
    def builtInCommented(self, s):
        # split s into individual words
        list_s = s.split(" ")
        # reverse each word in the list and add them to a new list
        list_s_reversed = [word[::-1] for word in list_s]
        # join those reversed words back on a space
        return ' '.join(list_s_reversed)

print(Solution().twoPointersWay('Hello there'))