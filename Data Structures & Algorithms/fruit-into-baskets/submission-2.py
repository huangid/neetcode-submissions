class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        total = 0
        l = 0
        m = {}
        for r in range(len(fruits)):
            while len(m) == 2 and fruits[r] not in m.keys():
                m[fruits[l]] -= 1
                if m[fruits[l]] == 0:
                    del m[fruits[l]]
                l += 1
            if fruits[r] not in m.keys():
                m[fruits[r]] = 0
            m[fruits[r]] += 1
            total = max(total, r - l + 1)
        return total