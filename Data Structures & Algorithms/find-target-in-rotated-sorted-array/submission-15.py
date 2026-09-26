class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(v, last):
            if v > last and v > target > last:
                return True
            elif v <= last and (target < v or target > last):
                return True
            return False
        l = 0
        r = len(nums) - 1
        last = nums[-1]
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif find(nums[m], last):
                r = m - 1
            else:
                l = m + 1
        return -1