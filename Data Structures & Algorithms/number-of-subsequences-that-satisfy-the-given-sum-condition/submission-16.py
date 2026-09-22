class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = 0
        MOD = 10**9 + 7
        nums.sort()
        r = len(nums) - 1
        l = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                n = (n+2**(r-l)) % MOD
                l += 1
            else:
                r -= 1
        return n