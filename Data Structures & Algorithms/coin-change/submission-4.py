class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [[1e9] * (amount+1) for _ in range(n+1)]
        f[0][0] = 0
        for i, coin in enumerate(coins):
            for j in range(amount+1):
                if coin > j:
                    f[i+1][j] = f[i][j]
                else:
                    f[i+1][j] = min(f[i][j], f[i+1][j-coin] + 1)
        ans = f[n][amount]
        return ans if ans < 1e9 else -1