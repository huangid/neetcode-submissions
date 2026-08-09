class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        m = { "W":0 , "B":0 }
        for i in range(k):
            m[blocks[i]] += 1
        color = m["W"]
        l = 0
        for r in range(k, len(blocks)):
            m[blocks[l]] -= 1
            l += 1
            m[blocks[r]] += 1
            color = min(color, m["W"])
        return color