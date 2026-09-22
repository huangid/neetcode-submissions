class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = k * threshold
        l = 0
        curSum = sum(arr[:k-1])
        res = 0
        for r in range(k - 1, len(arr)):
            curSum += arr[r]
            if curSum >= total:
                res += 1
            curSum -= arr[l]
            l += 1
        return res