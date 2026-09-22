class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weight = [-w for w in stones]
        heapq.heapify(weight)
        while len(weight) > 1:
            x = heapq.heappop(weight)
            y = heapq.heappop(weight)
            if x == y:
                continue
            elif x < y:
                y = -(y - x)
                heapq.heappush(weight, y)

        return -weight[0] if weight else 0
