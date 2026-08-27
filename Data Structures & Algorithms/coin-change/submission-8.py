class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i, t):
            if i == len(coins):
                return 0 if t == 0 else 1e9
            if (i, t) in cache:
                return cache[(i, t)]
            if coins[i] > t:
                cache[(i, t)] = dfs(i+1, t)
                return cache[(i, t)]
            cache[(i, t)] = min(dfs(i+1, t), 1 + dfs(i, t-coins[i]))
            return cache[(i, t)]
        res = dfs(0, amount)
        return res if res < 1e9 else -1