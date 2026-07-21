class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        length = 1e9
        for string in strs:
            length = min(length, len(string))

        l = 0
        for i in range(length):
            c = strs[0][i]
            for j in range(n):
                if c != strs[j][i]:
                    return strs[0][0:l]
            l += 1
        return strs[0][0:l]

