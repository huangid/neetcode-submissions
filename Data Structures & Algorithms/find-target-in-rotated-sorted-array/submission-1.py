class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        last = nums[r]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > last:
                l = mid + 1
            else:
                r = mid - 1
        
        if target > last:
            return self.find(nums[0:l], target)
        else:
            if self.find(nums[l:], target) == -1:
                return -1
            else:
                return l + self.find(nums[l:], target)


    def find(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1