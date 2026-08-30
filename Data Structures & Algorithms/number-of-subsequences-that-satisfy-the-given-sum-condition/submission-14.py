class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        MOD = 10**9 + 7
        res = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + 2**(r-l)) % MOD
                l += 1
            else:
                r -= 1
        return res