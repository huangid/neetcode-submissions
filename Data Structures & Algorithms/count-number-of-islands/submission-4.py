class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        h = len(grid)
        w = len(grid[0])
        def dfs(i, j):
            if i == -1 or i == h or j == -1 or j == w or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            for d in direction:
                r, c = d
                dfs(i+r, j+c)

        res = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res
