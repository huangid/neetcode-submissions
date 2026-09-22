class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = {}
        total = 0
        cursum = 0
        for n in nums:
            cursum += n
            diff = cursum - k
            if diff == 0:
                total += 1
            if diff in pre:
                total += pre[diff]
            if cursum not in pre:
                pre[cursum] = 0
            pre[cursum] += 1
            
        return total
        