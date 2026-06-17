class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def f(n):
            if n == len(nums):
                res.append(nums.copy())
            for i in range(n, len(nums)):
                nums[i], nums[n] = nums[n], nums[i]
                f(n+1)
                nums[i], nums[n] = nums[n], nums[i]
        f(0)
        return res