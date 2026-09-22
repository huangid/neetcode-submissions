class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        cache = {}
        def dfs(r, c):
            if r == h:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            path = triangle[r][c]
            path += min(dfs(r+1, c), dfs(r+1, c+1))
            cache[(r, c)] = path
            return path
        return dfs(0, 0)