# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available_letters = {}
        for char in magazine:
            available_letters[char] = available_letters.get(char, 0) + 1
        for letter in ransomNote:
            if letter in available_letters and available_letters[letter] >=1:
                available_letters[letter] -=1
            else:
                return False
        return True