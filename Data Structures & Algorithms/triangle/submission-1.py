class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        cache = {}
        def path(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == h - 1:
                return triangle[i][j]
            cache[(i, j)] = triangle[i][j] + min(path(i+1, j), path(i+1, j+1))
            return cache[(i, j)]
        return path(0, 0)