class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []
        def dfs(i):
            if i == n:
                res.append(path.copy())
                return
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return res