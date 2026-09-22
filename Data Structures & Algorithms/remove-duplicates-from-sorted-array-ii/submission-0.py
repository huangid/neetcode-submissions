class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(2, len(nums)):
            if nums[l-1] == nums[l] == nums[r]:
                continue
            l += 1
            nums[l] = nums[r]

        return l + 1
