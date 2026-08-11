class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = 0
        l = 0
        cursum = 0
        for r in range(k-1):
            cursum += arr[r]
        for r in range(k-1, len(arr)):
            cursum += arr[r]
            if cursum//k >= threshold:
                n += 1
            cursum -= arr[l]
            l += 1

        return n
            