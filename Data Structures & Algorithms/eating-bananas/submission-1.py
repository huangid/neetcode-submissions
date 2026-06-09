class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smin = 1
        smax = max(piles)
        while smin <= smax:
            mid = (smin + smax) // 2
            hr = 0
            for p in piles:
                hr += math.ceil(p/mid)
            if hr <= h:
                smax = mid - 1
            else:
                smin = mid + 1

        return smin