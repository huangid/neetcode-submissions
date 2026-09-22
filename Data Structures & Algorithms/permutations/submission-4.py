class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def dfs(s):
            if not s:
                res.append(path.copy())
                return
            for n in s:
                path.append(n)
                dfs(s-{n})
                path.pop()
        dfs(set(nums))
        return res