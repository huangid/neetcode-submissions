class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] not in nums[:j]:
                nums[j] = nums[i]
                j += 1

        return j
