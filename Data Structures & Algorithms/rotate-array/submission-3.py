class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums) - k
        for i in range(n):
            nums.append(nums[i])

        nums[:] = nums[n:]