class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        r = 0
        maxVal = nums[0]
        minVal = nums[0]
        res = 0
        while r < len(nums):
            maxVal = max(nums[l:r+1])
            minVal = min(nums[l:r+1])
            if maxVal - minVal <= limit:
                res = max(res, r - l + 1)
                r += 1
            else:
                l += 1
        return res