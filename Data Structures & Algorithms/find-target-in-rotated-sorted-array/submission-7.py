class Solution:
    def search(self, nums: List[int], target: int) -> int:
        last = nums[-1]
        l = 0
        r = len(nums) - 1
        def f(m):
            if nums[m] > last and nums[m] > target > last:
                return True
            elif nums[m] <= last and (target > last or target < nums[m]):
                return True
            return False
        while l <= r:
            m = (l+r)//2
            if f(m):
                r = m - 1
            else:
                l = m + 1
        return r if nums[r] == target else -1