# https://leetcode.com/problems/student-attendance-record-i/
class Solution:
    # O(n) Time | O(1) Space
    def checkRecord(self, s: str) -> bool:
        absent = 0
        for i in range(len(s)):
            if s[i] == 'A':
                absent += 1
                if absent ==2:
                    return False
            elif s[i] == 'L' and i < len(s) - 2:
                if s[i+1] == 'L' and s[i+2] == 'L':
                    return False
        return True
    def commented(self, s: str) -> bool:
        # set up counter for number of absences
        absent = 0
        # loop over each idx
        for i in range(len(s)):
            # if we have an absence -- update counter
            if s[i] == 'A':
                absent += 1
                # if counter reaches 2, no longer eligible
                if absent == 2:
                    return False
            # if we have an L with the possibility of having 2
            # trailing Ls, check to see if we have 3 in a row
            # if so, ineligible
            elif s[i] == 'L' and i < len(s) - 2:
                if s[i+1] == 'L' and s[i+2] == 'L':
                    return False
        # if we made it through, we're eligible!
        return True