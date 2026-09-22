class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        if n == 0:
            return []
        res, path = [], []
        def dfs(i):
            if i == n:
                res.append(''.join(path))
                return
            idx = int(digits[i])
            for c in m[idx]:
                path.append(c)
                dfs(i+1)
                path.pop()
        dfs(0)
        return res