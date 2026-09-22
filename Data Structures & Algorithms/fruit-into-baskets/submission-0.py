class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        res = 0
        f = {}
        for r in range(len(fruits)):
            f[fruits[r]] = f.get(fruits[r], 0) + 1
            while len(f.keys()) > 2:
                f[fruits[l]] -= 1
                if f[fruits[l]] == 0:
                    del f[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
