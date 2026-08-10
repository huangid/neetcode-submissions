class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        peri = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        peri += 1
                    if i == h - 1 or grid[i+1][j] == 0:
                        peri += 1
                    if j == 0 or grid[i][j-1] == 0:
                        peri += 1
                    if j == w - 1 or grid[i][j+1] == 0:
                        peri += 1
        return peri
