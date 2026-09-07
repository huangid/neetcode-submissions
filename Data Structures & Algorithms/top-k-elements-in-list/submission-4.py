class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = []
        for key, val in cnt.items():
            heapq.heappush(heap, (-val, key))
        res = []
        for _ in range(k):
            val, key = heapq.heappop(heap)
            res.append(key)
        return res