class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        minJ, maxJ = 0, 0
        while maxJ != len(nums) - 1:
            jumps += 1
            t = maxJ
            for i in range(minJ, maxJ + 1):
                maxJ = max(nums[i] + i, maxJ)
                maxJ = min(maxJ, len(nums) - 1)
            minJ = t + 1
        return jumps