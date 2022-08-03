from typing import List
#Nothing here yet
# Crappy n^2 Time n space solution
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                n.append(matrix[i][j])
        n.sort()
        return n[k-1]
        