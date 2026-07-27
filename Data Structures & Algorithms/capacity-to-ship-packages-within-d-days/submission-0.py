class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = (l+r) // 2
            d = self.numOfDays(weights, m)
            if d > days:
                l = m + 1
            else:
                r = m - 1
        return l

    def numOfDays(self, weights, capacity):
        c = capacity
        d = 1
        for w in weights:
            if c >= w:
                c -= w
            else:
                c = capacity - w
                d += 1
        return d