class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {} # char:latestIndex
        for i, c in enumerate(s):
            m[c] = i
        res = []
        i = 0
        prev = 0
        while i < len(s):
            j = m[s[i]]
            while True:
                if i == j:
                    break
                if m[s[i]] > j:
                    j = m[s[i]]
                i += 1
            i += 1
            res.append(j-prev+1)
            prev = i
        return res