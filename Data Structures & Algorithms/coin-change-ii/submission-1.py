class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i, t):
            if i == len(coins):
                return 1 if t == 0 else 0
            if (i, t) in cache:
                return cache[(i, t)]
            if coins[i] > t:
                cache[(i, t)] = dfs(i+1, t)
                return cache[(i, t)]
            cache[(i, t)] = dfs(i+1, t) + dfs(i, t-coins[i])
            return cache[(i, t)]
        return dfs(0, amount)