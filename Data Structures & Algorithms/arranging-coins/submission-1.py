class Solution:
    def arrangeCoins(self, n: int) -> int:
        compl = 0
        i = 1
        while n >= 0:
            compl += 1
            n -= i
            i += 1

        return compl-1