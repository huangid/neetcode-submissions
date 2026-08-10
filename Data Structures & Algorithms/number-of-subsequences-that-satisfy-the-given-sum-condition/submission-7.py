class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        nums.sort()
        MOD = 10**9 + 7
        minVal = nums[l]
        maxVal = nums[r]
        num = 0
        while l <= r:
            if nums[r] + nums[l] > target:
                r -= 1
            else:
                num = (num + 2**(r - l)) % MOD
                l += 1

        return num
        