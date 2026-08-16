class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAP = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if not digits:
            return []
        res = []
        path = []
        n = len(digits)
        def dfs(i):
            if i == n:
                res.append("".join(path))
                return
            d = int(digits[i])
            for j in range(len(MAP[d])):
                path.append(MAP[d][j])
                dfs(i+1)
                path.pop()
        dfs(0)
        return res