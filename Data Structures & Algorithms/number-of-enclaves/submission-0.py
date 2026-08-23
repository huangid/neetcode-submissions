class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        def dfs(i, j):
            if i == -1 or i == h or j == -1 or j == w or grid[i][j] == 0 or grid[i][j] == 2:
                return
            grid[i][j] = 2
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(h):
            for j in range(w):
                if i == 0 or j == 0 or i == h - 1 or j == w - 1:
                    if grid[i][j] == 1:
                        dfs(i, j)
        res = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    res += 1
        return res