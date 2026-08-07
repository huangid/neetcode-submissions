class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        for f in count.values():
            heap.append(-f)

        heapq.heapify(heap)
        time = 0
        queue = deque()
        while heap or queue:
            time += 1
            if heap:
                f = heapq.heappop(heap)
                f += 1
                if f != 0:
                    queue.append((f, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time