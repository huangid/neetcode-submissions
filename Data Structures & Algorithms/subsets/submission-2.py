class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        level = []
        def dfs(i):
            if i == len(nums):
                res.append(level.copy())
                return
            dfs(i+1)
            level.append(nums[i])
            dfs(i+1)
            level.pop()

        dfs(0)
        return res
