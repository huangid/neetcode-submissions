class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []
        n = len(digits)
        path = [''] * n
        if n == 0:
            return []

        def f(i):
            if i == n:
                res.append(''.join(path))
                return
            for c in m[int(digits[i])]:
                path[i] = c
                f(i+1)
        f(0)
        return res