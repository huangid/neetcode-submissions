class Solution:
    def jump(self, nums: List[int]) -> int:
        i = len(nums) - 1
        jump = 0

        while i > 0:
            for j in range(i):
                if j + nums[j] >= i:
                    i = j
                    jump += 1
                    break
        return jump
