class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        n = len(nums)
        def dfs(i, curSum):
            if curSum == target:
                res.append(path.copy())
                return
            if i == n or curSum > target:
                return
            path.append(nums[i])
            dfs(i, curSum + nums[i])
            path.pop()
            dfs(i+1, curSum)
        dfs(0, 0)
        return res