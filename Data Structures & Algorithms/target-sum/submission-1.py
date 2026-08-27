class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # p-(s-p) = t, 2p = t+s
        pos = target + sum(nums)
        if pos % 2 == 1 or pos < 0:
            return 0
        pos = pos // 2

        cache = {}
        def dfs(i, t):
            if i == len(nums):
                return 1 if t == 0 else 0
            if (i, t) in cache:
                return cache[(i, t)]
            if nums[i] > t:
                cache[(i, t)] = dfs(i+1, t)
                return cache[(i, t)]
            cache[(i, t)] = dfs(i+1, t) + dfs(i+1, t-nums[i])
            return cache[(i, t)]
        return dfs(0, pos)
