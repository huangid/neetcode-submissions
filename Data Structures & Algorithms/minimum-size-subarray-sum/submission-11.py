class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = 1e9
        cur = 0
        for r in range(len(nums)):
            cur += nums[r]
            while cur - nums[l] >= target:
                cur -= nums[l]
                l += 1
            if cur >= target:
                res = min(res, r - l + 1)
        return res if res <= len(nums) else 0