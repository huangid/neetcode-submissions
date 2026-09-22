class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        m = Counter(tasks)
        for num in m.values():
            heapq.heappush(heap, -num)
        q = deque()
        time = 0
        while heap or q:
            if q and time - q[0][0] > n:
                t, num = q.popleft()
                heapq.heappush(heap, num)
            if not heap:
                time += 1
                continue
            num = heapq.heappop(heap)
            num += 1
            if num != 0:
                q.append((time, num))
            time += 1
        return time
            
