class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        val = nums[r]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > val:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]