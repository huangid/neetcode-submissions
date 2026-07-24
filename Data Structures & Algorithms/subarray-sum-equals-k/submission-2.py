class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = {0:1}
        n = len(nums)
        res = curSum = 0
        for num in nums:
            curSum += num
            diff = curSum - k
            if diff in m:
                res += m[diff]
            m[curSum] = m.get(curSum, 0) + 1
        return res