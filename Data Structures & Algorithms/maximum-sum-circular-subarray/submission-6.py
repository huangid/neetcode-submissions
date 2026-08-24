class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)
        curSum = 0
        minSum = nums[0]
        for n in nums:
            if curSum > 0:
                curSum = 0
            curSum += n
            minSum = min(minSum, curSum)
        maxSum2 = sum(nums) - minSum
        if maxSum < 0:
            return maxSum
        res = max(maxSum, maxSum2)
        return res