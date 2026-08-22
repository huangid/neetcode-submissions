class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = -1e9
        for r in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[r]
            maxSum = max(curSum, maxSum)
        return maxSum