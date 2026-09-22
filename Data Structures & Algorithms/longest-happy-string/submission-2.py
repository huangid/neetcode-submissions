class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a != 0:
            heapq.heappush(heap, (-a, 'a'))
        if b != 0:
            heapq.heappush(heap, (-b, 'b'))
        if c != 0:
            heapq.heappush(heap, (-c, 'c'))
        res = []
        while heap:
            n, c = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == res[-2] == c:
                if heap:
                    n1, c1 = heapq.heappop(heap)
                    heapq.heappush(heap, (n, c))
                    n, c = n1, c1
                else:
                    return "".join(res)
            n += 1
            res.append(c)
            if n != 0:
                heapq.heappush(heap, (n, c))
        return "".join(res)