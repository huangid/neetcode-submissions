class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []

        def dfs(i, curSum):
            if curSum == target:
                res.append(path.copy())
                return
            if curSum > target or i == len(nums):
                return
            dfs(i+1, curSum)
            path.append(nums[i])
            dfs(i, curSum + nums[i])
            path.pop()

        dfs(0, 0)
        return res