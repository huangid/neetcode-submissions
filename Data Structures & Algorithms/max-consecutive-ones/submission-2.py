class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        p = 0
        for n in nums:
            if n == 1:
                p += 1
            else:
                m = max(p, m)
                p = 0

        return max(p, m)