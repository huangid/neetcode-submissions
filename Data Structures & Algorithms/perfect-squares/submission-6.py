class Solution:
    def numSquares(self, n: int) -> int:
        start = int(n**0.5)
        cache = {}
        def dfs(i, cur):
            if cur == 0:
                return 0
            if i == 0:
                return 1e9
            if (i, cur) in cache:
                return cache[(i, cur)]
            ans = 1e9
            if i**2 <= cur:
                ans = dfs(i, cur-i**2) + 1
            cache[(i, cur)] = min(ans, dfs(i-1, cur))
            return cache[(i, cur)]
        num = dfs(start, n)
        return num