class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def linear(nums):
            prev2 = 0
            prev1 = 0
            for i in range(len(nums)):
                cur = max(prev2+nums[i], prev1)
                prev2, prev1 = prev1, cur
            return prev1
        
        return max(linear(nums[:-1]), linear(nums[1:]))

        