class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        s = set(nums)
        def dfs(i, s):
            if i == len(nums):
                res.append(path.copy())
                return
            for num in s:
                path.append(num)
                dfs(i+1, s - {num})
                path.pop()
        dfs(0, s)
        return res