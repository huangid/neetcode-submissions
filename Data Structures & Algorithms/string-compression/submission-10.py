class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        while r < len(chars):
            s = r
            while r < len(chars) - 1 and chars[r] == chars[r+1]:
                r += 1
            length = r - s + 1
            chars[l] = chars[s]
            l += 1
            if length > 1:
                for c in str(length):
                    chars[l] = c
                    l += 1
            r += 1
        return l
            