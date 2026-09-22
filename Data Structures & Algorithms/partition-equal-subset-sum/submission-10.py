class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        part = s // 2
        def dfs(i, curSum):
            if curSum == part:
                return True
            if i == len(nums):
                return False
            res = dfs(i+1, curSum+nums[i]) or dfs(i+1, curSum)
            return res
        return dfs(0, 0)