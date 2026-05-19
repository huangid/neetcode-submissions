class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            while left <= right:
                mid = (left+right) // 2
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    return mid
            return -1
        
        last = nums[-1]
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if last < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        l = l % len(nums)
        if target > last:
            return binary_search(0, l - 1)
        else:
            return binary_search(l, len(nums)-1)