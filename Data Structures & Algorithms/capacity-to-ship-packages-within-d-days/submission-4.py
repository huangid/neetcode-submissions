class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def time(w):
            t = 1
            cur = 0
            for v in weights:
                if cur + v > w:
                    t += 1
                    cur = v
                else:
                    cur += v
            return t
        low = max(weights)
        high = sum(weights)
        while low <= high:
            m = (low+high) // 2
            if time(m) > days:
                low = m + 1
            else:
                high = m - 1
        return low
        