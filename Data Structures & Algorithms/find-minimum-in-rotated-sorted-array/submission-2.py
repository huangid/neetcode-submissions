class Solution:
    def findMin(self, nums: List[int]) -> int:
        last = nums[-1]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] > last:
                l = m + 1
            else:
                r = m - 1
        return nums[l]