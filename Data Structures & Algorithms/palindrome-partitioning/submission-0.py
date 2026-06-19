class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        n = len(s)

        def f(i):
            if i == n:
                res.append(path.copy())
                return
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    path.append(s[i:j+1])
                    f(j+1)
                    path.pop()
        f(0)
        return res