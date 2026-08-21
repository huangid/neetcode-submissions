class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = []
        for i, val in enumerate(nums):
            arr.append([val, i])
        heapq.heapify(arr)
        res = [0] * len(nums)
        for _ in range(k):
            x, i = heapq.heappop(arr)
            heapq.heappush(arr, [x*multiplier, i])
        for x, i in arr:
            res[i] = x
        return res