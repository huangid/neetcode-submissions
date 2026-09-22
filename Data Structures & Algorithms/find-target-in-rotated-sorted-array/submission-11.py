class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check(m):
            if nums[m] > last and nums[m] > target > last:
                return True
            elif nums[m] <= last and (target > last or target < nums[m]):
                return True
            return False

        last = nums[-1]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return -1