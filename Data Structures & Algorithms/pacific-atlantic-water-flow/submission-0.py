class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        h = len(heights)
        w = len(heights[0])
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        def dfs(r, c):
            if (r, c) in visit:
                return
            visit.add((r, c))
            if r == 0 or c == 0:
                pac.add((r, c))
            if r == h-1 or c == w-1:
                atl.add((r, c))
            for dr, dc in direction:
                if 0 <= r + dr < h and 0 <= c + dc < w and heights[r][c] >= heights[r+dr][c+dc]:
                    dfs(r+dr, c+dc)
                else:
                    continue
                if (r+dr, c+dc) in pac:
                    pac.add((r, c))
                if (r+dr, c+dc) in atl:
                    atl.add((r, c))
        for i in range(h):
            for j in range(w):
                dfs(i, j)
        res = []
        for i in range(h):
            for j in range(w):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res


            