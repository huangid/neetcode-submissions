class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        h, w = len(heights), len(heights[0])

        def dfs(i, j, ocean):
            if (i, j) in ocean:
                return
            ocean.add((i, j))
            for dr, dc in direction:
                if 0 <= i+dr < h and 0 <= j+dc < w:
                    if heights[i+dr][j+dc] >= heights[i][j]:
                        dfs(i+dr, j+dc, ocean)

        for i in range(h):
            for j in range(w):
                if i == 0 or j == 0:
                    dfs(i, j, pac)
                if i == h - 1 or j == w - 1:
                    dfs(i, j, atl)

        res = []
        for i in range(h):
            for j in range(w):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res
