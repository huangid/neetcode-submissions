class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        def dfs(i, s):
            if i == n:
                res.append(path.copy())
                return
            for c in s:
                path.append(c)
                dfs(i+1, s-{c})
                path.pop()
        dfs(0, set(nums))
        return res