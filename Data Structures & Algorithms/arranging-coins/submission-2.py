class Solution:
    def arrangeCoins(self, n: int) -> int:
        r = 0
        i = 1
        while n >= i:
            n -= i
            i += 1
            r += 1
        return r