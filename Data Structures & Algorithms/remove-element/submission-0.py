class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l = 0
        for i in range(n):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l

