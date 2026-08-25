class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        def dfs(i, j):
            if i == -1 or i == h or j == -1 or j == w or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1
            area += dfs(i+1, j)
            area += dfs(i-1, j)
            area += dfs(i, j+1)
            area += dfs(i, j-1)
            return area
        res = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res