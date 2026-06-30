from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @lru_cache
        def f(i, c):
            if c == 0:
                return 0
            if i < 0:
                return 1e9
            if coins[i] > c:
                return f(i-1, c)
            return min(f(i-1, c), f(i, c-coins[i])+1)
        num = f(n-1, amount)
        return -1 if num is 1e9 else num