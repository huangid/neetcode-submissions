class Solution:
    def reorganizeString(self, s: str) -> str:
        m = Counter(s)
        heap = []
        res = []
        for c, v in m.items():
            heapq.heappush(heap, (-v, c))
        while len(res) != len(s):
            v, c = heapq.heappop(heap)
            if res and res[-1] == c:
                if not heap:
                    return ""
                v1, c1 = heapq.heappop(heap)
                heapq.heappush(heap, (v, c))
                v, c = v1, c1
            v += 1
            res.append(c)
            if v != 0:
                heapq.heappush(heap, (v, c))
        return "".join(res)
            
