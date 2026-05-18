class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        prof = 0
        for i, price in enumerate(prices):
            if price < prices[buy]:
                buy = i
            else:
                prof = max(prof, price - prices[buy])

        return prof
