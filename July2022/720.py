# https://leetcode.com/problems/meeting-rooms/

# O(n*logn) Time | O(n) Space
# NOTE: python sort uses linear space during recursion
def meetingOverlap(intervals):
    intervals.sort()
    for i in range(len(intervals)-1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
    return True

# Commented Version
def meetingOverlap(intervals):
    # sort the intervals so we can see all of our meetings in a linear fashion
    intervals.sort()
    # loop over each meeting
    for i in range(len(intervals)-1):
        # compare the current meeting's end time with the next meetings start time
        # if it is > start time of next meeting, we can't make it
        if intervals[i][1] > intervals[i+1][0]:
            return False
    # if we never found an overlap, we make it thru all meetings
    return True