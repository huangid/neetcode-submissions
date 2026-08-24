class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        hi = len(nums) - 1
        while hi > 0 and nums[hi] == nums[0]:
            hi -= 1
        end = nums[hi]
        def check(i):
            if nums[i] > end:
                return target > end and nums[i] >= target
            else:
                return target > end or nums[i] >= target

        l = 0
        r = hi
        while l <= r:
            mid = (l+r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l <= len(nums) and nums[l] == target