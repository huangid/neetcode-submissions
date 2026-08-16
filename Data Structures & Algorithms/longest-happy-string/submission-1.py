class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        heap = []
        if a:
            heapq.heappush(heap, [-a, 'a'])
        if b:
            heapq.heappush(heap, [-b, 'b'])
        if c:
            heapq.heappush(heap, [-c, 'c'])
        for i in range(a+b+c):
            n, ch = heapq.heappop(heap)
            if i > 1 and res[-1] == res[-2] == ch:
                if not heap:
                    return "".join(res)
                n1, ch1 = heapq.heappop(heap)
                heapq.heappush(heap, [n, ch])
                n, ch = n1, ch1
            n += 1
            res.append(ch)
            if n != 0:
                heapq.heappush(heap, [n, ch])
        return "".join(res)
            