class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for g in gifts:
            heapq.heappush(heap, -g)
        for _ in range(k):
            g = -heapq.heappop(heap)
            heapq.heappush(heap, -int(g**0.5))
        return -sum(heap)