class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        def dfs(val, sqrt):
            if sqrt == 0:
                return 0 if val == 0 else 1e9
            if (val, sqrt) in cache:
                return cache[(val, sqrt)]
            if sqrt**2 > val:
                cache[(val, sqrt)] = dfs(val, sqrt-1)
            else:
                cache[(val, sqrt)] = min(1+dfs(val-sqrt**2, sqrt), dfs(val, sqrt-1))
            return cache[(val, sqrt)]
        return dfs(n, int(n**0.5))