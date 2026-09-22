class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x*x + y*y
            heap.append([dist, x, y])
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            d, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res