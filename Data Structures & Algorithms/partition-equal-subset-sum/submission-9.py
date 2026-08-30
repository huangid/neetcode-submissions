class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2

        cache = {}

        def dfs(i, t):
            if t == 0:
                return True
            if t < 0 or i == len(nums):
                return False
            if (i, t) in cache:
                return cache[(i, t)]
            cache[(i, t)] = dfs(i + 1, t) or dfs(i + 1, t - nums[i])
            return cache[(i, t)]

        return dfs(0, target)
