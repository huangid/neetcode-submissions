class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        prof = 0
        for i, price in enumerate(prices):
            if price < prices[b]:
                b = i
            else:
                prof = max(prof, price - prices[b])

        return prof
