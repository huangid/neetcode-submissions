class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        window = ""
        length = float('inf')
        t_count = Counter(t)
        for i in range(len(s)):
            sub = s[l:i+1]
            while all(Counter(sub)[c] >= t_count[c] for c in t_count):
                if (length > len(sub)):
                    window = sub
                    length = min(len(sub), length)
                l += 1
                sub = s[l:i+1]
        return window