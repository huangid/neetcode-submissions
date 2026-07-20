class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        output = nums[-1]
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = nums[i]
            output = max(output, dp[i][i])
            for j in range(i+1, n):
                dp[i][j] = nums[j] * dp[i][j-1]
                output = max(output, dp[i][j])

        return output