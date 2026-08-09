class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num = 1
        while True:
            if num not in nums:
                return num
            num += 1