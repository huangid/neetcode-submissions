class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        i = 1
        while i <= len(nums)-1:
            prev = nums[k-1]
            while i <= len(nums)-1 and nums[i] == prev:
                i += 1
            if i <= len(nums)-1:
                nums[k] = nums[i]
                k += 1
        return k