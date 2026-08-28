class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}
        def dfs(i, j):
            if i == j:
                return 1
            elif j + 1 == i:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if s[i] == s[j]:
                cache[(i, j)] = 2 + dfs(i+1, j-1)
            else:
                cache[(i, j)] = max(dfs(i, j-1), dfs(i+1, j))
            return cache[(i, j)]
        return dfs(0, len(s) - 1)