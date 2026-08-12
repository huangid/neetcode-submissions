class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        length = 1e9
        cursum = 0
        for r in range(len(nums)):
            cursum += nums[r]
            while cursum >= target:
                length = min(length, r - l + 1)
                cursum -= nums[l]
                l += 1
        return length if length < 1e9 else 0