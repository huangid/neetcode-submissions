class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2

        cache = {}
        def dfs(i, t):
            if (i, t) in cache:
                return cache[(i, t)]
            if t == 0:
                cache[(i, t)] = True
                return True
            if t < 0 or i == len(nums):
                cache[(i, t)] = False
                return False
            cache[(i, t)] = dfs(i+1, t) or dfs(i+1, t-nums[i])
            return cache[(i, t)]
        
        return dfs(0, target)