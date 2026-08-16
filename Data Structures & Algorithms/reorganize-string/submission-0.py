class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        heap = []
        for k, num in c.items():
            heapq.heappush(heap, [-num, k])
        last = None
        res = []
        for _ in range(len(s)):
            num, k = heapq.heappop(heap)
            if k == last:
                if heap:
                    num1, k1 = heapq.heappop(heap)
                else:
                    return ""
                heapq.heappush(heap, [num, k])
                num, k = num1, k1
            last = k
            res.append(k)
            num += 1
            if num != 0:
                heapq.heappush(heap, [num, k])
        return "".join(res)


            