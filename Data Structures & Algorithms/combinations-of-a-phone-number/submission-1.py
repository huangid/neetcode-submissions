class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAP = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        path = []
        res = []
        if len(digits) == 0:
            return []

        def dfs(i):
            if i == len(digits):
                res.append(''.join(path))
                return

            for c in MAP[int(digits[i])]:
                path.append(c)
                dfs(i+1)
                path.pop()

        dfs(0)
        return res