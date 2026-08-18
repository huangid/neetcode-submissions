class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda i:i[1])
        total = 0
        heap = []
        for trip in trips:
            dist = trip[1]
            heapq.heappush(heap, [trip[2], trip[0]])
            while heap and heap[0][0] <= dist:
                to, num = heapq.heappop(heap)
                total -= num
            total += trip[0]
            if total > capacity:
                return False
        return True
