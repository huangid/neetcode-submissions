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
            v, c = heapq.heappop(heap)
            if len(res) >= 2 and c == res[-1] == res[-2]:
                if heap:
                    tv, tc = heapq.heappop(heap)
                    heapq.heappush(heap, (v, c))
                    v, c = tv, tc
                else:
                    return "".join(res)
            v += 1
            res.append(c)
            if v != 0:
                heapq.heappush(heap, (v, c))
        return "".join(res)
            
