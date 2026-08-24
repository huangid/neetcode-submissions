class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = curMin = 0
        maxSum = minSum = nums[0]
        for n in nums:
            curMax = max(curMax, 0)
            curMax += n
            maxSum = max(maxSum, curMax)
        for n in nums:
            curMin = min(curMin, 0)
            curMin += n
            minSum = min(minSum, curMin)
        maxSum2 = sum(nums) - minSum
        if maxSum < 0:
            return maxSum
        res = max(maxSum, maxSum2)
        return res