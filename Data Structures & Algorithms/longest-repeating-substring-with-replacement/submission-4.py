class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        m = {}
        length = 1
        maxf = 0
        for i, char in enumerate(s):
            m[char] = m.get(char, 0) + 1
            maxf = max(m[char], maxf)
            while i - left + 1 - maxf > k:
                m[s[left]] = m[s[left]] - 1
                left += 1

            length = max(length, sum(m.values()))

        return length