class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        h = len(grid)
        w = len(grid[0])

        def dfs(i, j):
            if i == -1 or i == h or j == -1 or j == w or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0

            visit.add((i, j))
            p = dfs(i+1, j)
            p += dfs(i-1, j)
            p += dfs(i, j+1)
            p += dfs(i, j-1)
            return p
        for i in range(h):
            for j in range(w):
                if grid[i][j]:
                    return dfs(i, j)