class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            res = 1e9
            for c in coins:
                if amount >= c:
                    res = min(res, 1 + dfs(amount-c))
                cache[amount] = res
            return res
        return -1 if dfs(amount) >= 1e9 else dfs(amount)