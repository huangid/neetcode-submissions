class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        cache = {}
        def dfs(i, j):
            if i == n1 and j == n2 and i+j == n3:
                return True
            if (i, j) in cache:
                return cache[(i, j)]
            ans = False
            if i < n1 and i+j < n3 and s3[i+j] == s1[i]:
                ans = dfs(i+1, j)
            if not ans and j < n2 and i+j < n3 and s3[i+j] == s2[j]:
                ans = dfs(i, j+1)
            cache[(i, j)] = ans
            return ans

        return dfs(0, 0)