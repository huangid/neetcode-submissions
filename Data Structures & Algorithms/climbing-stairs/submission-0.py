class Solution:
    def climbStairs(self, n: int) -> int:
        m = {}
        def f(i):
            if i in m:
                return m[i]
            if i == 1:
                return 1
            if i == 2:
                return 2
            res = f(i-1) + f(i-2)
            m[i] = res
            return res
        return f(n)