class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i, cur):
            if cur > amount:
                return 1e9
            if i == len(coins):
                return 0 if cur == amount else 1e9
            if (i, cur) in cache:
                return cache[(i, cur)]
            cache[(i, cur)] = min(dfs(i, cur+coins[i])+1, dfs(i+1, cur))
            return cache[(i, cur)]
        res = dfs(0, 0)
        return res if res < 1e9 else -1