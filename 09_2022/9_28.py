from typing import List
# https://leetcode.com/problems/relative-ranks/
# O(n log n) Time | O(n) Space
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pos_dict = {}
        new = sorted(score, reverse=True)
        for i in range(len(new)):
            if i > 2:
                pos_dict[new[i]] = str(i+1)
            elif i == 0:
                pos_dict[new[i]] = 'Gold Medal'
            elif i == 1:
                pos_dict[new[i]] = 'Silver Medal'
            else:
                pos_dict[new[i]] = 'Bronze Medal'
        return [pos_dict[num] for num in score]
    def commented(self, score: List[int]) -> List[str]:
        # create a dict for each relative position
        pos_dict = {}
        # sort the scores from highest to lowest
        new = sorted(score, reverse=True)
        # loop over each index
        for i in range(len(new)):
            # the places after idx two are just the idx + 1
            # example: i = 3 is 4th place
            if i > 2:
                pos_dict[new[i]] = str(i+1)
            # 0th position is Gold
            elif i == 0:
                pos_dict[new[i]] = 'Gold Medal'
            # 1st is Silver
            elif i == 1:
                pos_dict[new[i]] = 'Silver Medal'
            # 2nd is Bronze
            else:
                pos_dict[new[i]] = 'Bronze Medal'
        # grab each value (place) for each score in the OG list
        return [pos_dict[num] for num in score]

    def timeSpaceCommented(self, score: List[int]) -> List[str]:
        pos_dict = {} # O(n) Space as we fill it with positions below
        new = sorted(score, reverse=True) # O(n log n) Time to sort + O(n) Space for new array
        for i in range(len(new)): # O(n) Time
            # all below are O(1) Time but do contribute to the space we talked about in the dictionary
            if i > 2:
                pos_dict[new[i]] = str(i+1)
            elif i == 0:
                pos_dict[new[i]] = 'Gold Medal'
            elif i == 1:
                pos_dict[new[i]] = 'Silver Medal'
            else:
                pos_dict[new[i]] = 'Bronze Medal'
        return [pos_dict[num] for num in score] # O(n) time and space to iterate and create another new arr