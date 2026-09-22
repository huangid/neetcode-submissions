class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        m = {}
        for i, v in enumerate(s):
            m[v] = i
        l, r = 0, 0
        end = 0
        while r < len(s):
            end = max(end, m[s[r]])
            if end == r:
                res.append(r-l+1)
                l = r + 1
            r += 1
        return res