class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        MOD = (10**9) + 7
        for i, left in enumerate(nums):
            r = n - 1
            while left + nums[r] > target and i <= r:
                r -= 1
            if i <= r:
                res = (res + (2**(r-i)))%MOD

        return res
