# https://leetcode.com/problems/student-attendance-record-i/
class Solution:
    # O(n) Time | O(1) Space
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late_count = 0
        for mark in s:
            if mark == 'A':
                absent += 1
                late_count = 0
                if absent ==2:
                    return False
            elif mark == 'L':
                late_count += 1
                if late_count == 3:
                    return False
            else:
                late_count = 0
        return True
    def commented(self, s: str) -> bool:
        # set up counters for absences and consecutive L's
        absent = 0
        late_count = 0
        # loop over every char
        for mark in s:
            # if a mark is == 'A', reset consecutive L's
            # and add one to absences
            if mark == 'A':
                absent += 1
                late_count = 0
                # 2 absences is ineligible
                if absent == 2:
                    return False
            # if we have an L, increment consecutive late count
            elif mark == 'L':
                late_count += 1
                # if we hit 3 -- ineligible
                if late_count == 3:
                    return False
            # if we have a P, also reset consecutive late count
            else:
                late_count = 0
        # we made it without triggering a false return, we're eligible!
        return True