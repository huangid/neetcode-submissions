class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        def num(cur, val):
            if cur == 0:
                return 0
            if cur < 0 or val == 0:
                return 1e9
            if (cur, val) in cache:
                return cache[(cur, val)]
            sqrt = val**2
            a = 1 + num(cur-sqrt, val)
            b = num(cur, val - 1)
            cache[(cur, val)] = min(a, b)
            return cache[(cur, val)]
        return num(n, int(n**0.5))
