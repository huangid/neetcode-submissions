class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        l = 0
        s = 0
        for r in range(n):
            s += nums[r]
            while s - nums[l] >= target:
                s -= nums[l]
                l += 1
            if s >= target:
                res = min(res, r-l+1)

        return res if res <= n else 0