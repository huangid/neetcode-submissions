class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        def dfs(r, c):
            if r == -1 or r == h or c == -1 or c == w or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            area += dfs(r-1, c)
            area += dfs(r+1, c)
            area += dfs(r, c-1)
            area += dfs(r, c+1)
            return area
        res = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res