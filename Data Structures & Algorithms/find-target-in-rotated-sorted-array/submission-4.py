class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check(i):
            end = nums[-1]
            if nums[i] > end:
                return target > end and nums[i] >= target
            else:
                return target > end or nums[i] >= target

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        if r == len(nums) or nums[l] != target:
            return -1

        return l
