class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        h = len(grid)
        w = len(grid[0])
        def island(i, j):
            visit.add((i, j))
            if i > 0 and grid[i-1][j] == "1" and (i-1, j) not in visit:
                island(i - 1, j)
            if i < h - 1 and grid[i+1][j] == "1" and (i+1, j) not in visit:
                island(i + 1, j)
            if j > 0 and grid[i][j-1] == "1" and (i, j-1) not in visit:
                island(i, j - 1)
            if j < w - 1 and grid[i][j+1] == "1" and (i, j+1) not in visit:
                island(i, j + 1)
            return
        res = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1" and (i, j) not in visit:
                    island(i, j)
                    res += 1
        return res