class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = [''] * 2 * n 

        def f(i, left):
            if i == 2 * n:
                res.append(''.join(path))
                return
            if left < n:
                path[i] = '('
                f(i+1, left+1)
            if i-left < left:
                path[i] = ')'
                f(i+1, left)
        f(0, 0)
        return res