class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * (len(nums) + 1)
        for i in range(len(nums) - 1):
            dp[i+2] = max(dp[i] + nums[i], dp[i+1])
        val1 = dp[-1]
        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i-1] + nums[i], dp[i])
        val2 = dp[-1]
        return max(val1, val2)