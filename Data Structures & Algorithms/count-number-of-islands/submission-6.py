class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h = len(grid)
        w = len(grid[0])
        def dfs(i, j):
            if i == -1 or i == h or j == -1 or j == w or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        res = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res