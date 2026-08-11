class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        m = {}
        length = 1
        for i, char in enumerate(s):
            m[char] = m.get(char, 0) + 1
            diff = sum(m.values()) - max(m.values())
            while diff > k:
                m[s[left]] = m[s[left]] - 1
                left += 1
                diff = sum(m.values()) - max(m.values())
            length = max(length, sum(m.values()))

        return length