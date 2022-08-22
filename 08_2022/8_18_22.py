from typing import List
# O(n log n) Time | O(n) Space
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        d = {}
        res = 0
        for num in arr:
            d[num] = d.get(num, 0) + 1
        sorted_values = sorted(d.values())
        while n > len(arr)/2:
            n -= sorted_values.pop()
            res +=1
        return res
    def minSetSizeCommented(self, arr: List[int]) -> int:
        # placeholder we will decrease list size as we remove numbers
        n = len(arr)
        # dict to count frequency of each number
        d = {}
        # counter for how many integers we have removed
        res = 0
        # fill dict as a number counter
        for num in arr:
            d[num] = d.get(num, 0) + 1
        # sort the values
        sorted_values = sorted(d.values())
        # while n is still more than half the list size
        while n > len(arr)/2:
            # decrease the list size by the highest frequency
            # higher frequency == smaller amount of nums we have to remove
            n -= sorted_values.pop()
            # add one number to the counter
            res +=1
        return res

# if you want to actually see the test cases in your editor
# or PythonTutor
s = Solution()
s.minSetSize([3,3,3,3,5,5,5,2,2,7])
s.minSetSize([7,7,7,7,7,7])
