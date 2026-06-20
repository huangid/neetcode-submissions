class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = []

        def valid(r, c):
            for R, C in enumerate(path):
                if R-C == r-c or R+C == r+c:
                    return False
            return True

        def f(r, s):
            if r == n:
                res.append(['.'*a + 'Q' + '.'*(n-1-a) for a in path])
                return
            for c in s:
                if valid(r, c):
                    path.append(c)
                    f(r+1, s-{c})
                    path.pop()
        f(0, set(range(n)))
        return res