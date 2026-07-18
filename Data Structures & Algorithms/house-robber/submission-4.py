class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        f = [-1] * n
        def dfs(i):
            if i >= n:
                return 0
            if f[i] != -1:
                return f[i]
            f[i] = nums[i] + max(dfs(i+2), dfs(i+3))
            return f[i]
        return max(dfs(0), dfs(1))