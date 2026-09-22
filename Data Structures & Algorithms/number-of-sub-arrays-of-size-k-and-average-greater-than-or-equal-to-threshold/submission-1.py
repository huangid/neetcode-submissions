class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = k * threshold
        res = 0
        curSum = 0
        for i in range(len(arr)):
            curSum += arr[i]
            if i >= k - 1:
                if curSum >= total:
                    res += 1
                curSum -= arr[i-k+1]
        return res
            