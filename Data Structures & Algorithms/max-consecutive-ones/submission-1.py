class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        p = 0
        for n in nums:
            if n == 1:
                p += 1
            else:
                res = max(res, p)
                p = 0
        return max(res, p)