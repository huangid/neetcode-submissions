class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        def dfs(i):
            if i == len(nums):
                res.append(path.copy())
                return
            dfs(i+1)
            path.append(nums[i])
            dfs(i+1)
            path.pop()

        dfs(0)
        return res