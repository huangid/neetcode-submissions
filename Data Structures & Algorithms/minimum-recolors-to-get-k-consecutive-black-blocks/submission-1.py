class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k - 1
        count = Counter(blocks[:k])
        mini = len(blocks)
        while r < len(blocks) - 1:
            mini = min(mini, count.get("W", 0))
            count[blocks[l]] -= 1
            l += 1
            r += 1
            val = count.get(blocks[r], 0)
            count[blocks[r]] = val + 1
            
        return min(mini, count.get("W", 0))
