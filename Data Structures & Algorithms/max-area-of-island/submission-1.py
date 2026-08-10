class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        h, w = len(grid), len(grid[0])
        dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j):
            if i == -1 or i == h or j == -1 or j == w or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            a = 1
            for r, c in dire:
                a += dfs(i+r, j+c)
            return a

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea

