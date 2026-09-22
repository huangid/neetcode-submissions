class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        heap = []
        for k, v in cnt.items():
            heap.append((-v, k))
        heapq.heapify(heap)
        res = []
        while heap:
            v, k = heapq.heappop(heap)
            if res and res[-1] == k:
                if heap:
                    v1, k1 = heapq.heappop(heap)
                    heapq.heappush(heap, (v, k))
                    v, k = v1, k1
                else:
                    return ""
            v += 1
            res.append(k)
            if v != 0:
                heapq.heappush(heap, (v, k))
        return ''.join(res)