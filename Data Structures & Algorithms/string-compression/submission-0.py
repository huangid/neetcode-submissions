class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        i = 0
        while i < len(chars):
            if i > 0 and chars[i] == chars[i-1]:
                j = i - 1
                while i < len(chars) and chars[i] == chars[i-1]:
                    i += 1
                length = i - j
                s = s + str(length)
            else:
                s = s + chars[i]
                i += 1
        m = len(s)
        for n in range(m):
            chars[n] = s[n]

        return m
            
