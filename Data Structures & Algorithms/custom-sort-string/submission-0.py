class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        m = Counter(s)
        for i in range(len(order)):
            if order[i] in m.keys():
                for j in range(m[order[i]]):
                    res.append(order[i])
                m[order[i]] = 0
        for k, v in m.items():
            if v != 0:
                for i in range(v):
                    res.append(k)
        return "".join(res)
                
        
