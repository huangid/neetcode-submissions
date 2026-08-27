class Solution:
    def search(self, nums: List[int], target: int) -> int:
        last = nums[-1]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] > last and last < target < nums[m]:
                r = m - 1
            elif nums[m] <= last and (target < nums[m] or target > last):
                r = m - 1
            else:
                l = m + 1
        return r if r < len(nums) and nums[r] == target else -1