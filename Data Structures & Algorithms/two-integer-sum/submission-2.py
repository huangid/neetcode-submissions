class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in table:
                return [table[need], i]
            table[num] = i

