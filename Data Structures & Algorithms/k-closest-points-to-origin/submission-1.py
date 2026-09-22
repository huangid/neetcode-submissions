class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i, p in enumerate(points):
            dist.append((-(p[0]*p[0]+p[1]*p[1]), i))
        
        heapq.heapify(dist)

        while len(dist) > k:
            heapq.heappop(dist)

        return [points[i] for d, i in dist]
