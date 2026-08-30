class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = 0
        n = 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                res[p] = nums[i]
                p += 2
            else:
                res[n] = nums[i]
                n += 2
        return res
                