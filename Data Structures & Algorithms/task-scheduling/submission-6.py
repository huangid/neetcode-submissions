class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        heap = []
        cnt = Counter(tasks)
        for c, v in cnt.items():
            heapq.heappush(heap, -v)
        time = 0
        while heap or q:
            if q and q[0][1] == time:
                v, t = q.popleft()
                heapq.heappush(heap, v)
            if heap:
                v = heapq.heappop(heap)
                v += 1
                if v != 0:
                    q.append((v, time+n+1))
            time += 1
        return time
