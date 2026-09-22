class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        res.append(chars[0])
        i = 1
        while i < len(chars):
            j = i
            if chars[j] == chars[i-1]:
                while j < len(chars) and chars[j] == chars[i-1]:
                    j += 1
                length = j - i + 1
                res.extend(str(length))
                i = j
            else:
                res.append(chars[i])
                i += 1

        for i in range(len(res)):
            chars[i] = res[i]
        return len(res)
