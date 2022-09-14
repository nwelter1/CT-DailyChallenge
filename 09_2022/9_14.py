# O(n*m) where n is rows, m is cols
# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

class Commented:
    def numIslands(self, grid):
        # edge case if there is no grid
        if not grid:
            return 0
        # initialize island counter
        count = 0
        # loop over every value in the matrix
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if we find a 1, trigger a dfs to updated all touching 1's
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    # once that dfs is complete, count that as one island
                    count += 1
        return count
    # dfs helper function
    def dfs(self, grid, i, j):
        # if we have stepped outside of the grid or run into a 0 or #, return
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        # if this is a 1, update to a placeholder so we don't count it again
        grid[i][j] = '#'
        # keep looking for more 1's in every direction!
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)