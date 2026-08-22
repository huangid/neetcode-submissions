class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def day(cap):
            day = 1
            cur = 0
            for w in weights:
                if cur + w > cap:
                    day += 1
                    cur = w
                else:
                    cur += w
            return day
        
        l = max(weights)
        r = sum(weights)

        while l <= r:
            m = (l+r) // 2
            if day(m) > days:
                l = m + 1
            else:
                r = m - 1
        return l