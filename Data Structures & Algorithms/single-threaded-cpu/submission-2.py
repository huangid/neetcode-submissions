class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        queue = []
        for i, t in enumerate(tasks):
            queue.append((t[0], t[1], i))
        queue.sort()
        queue = deque(queue)
        t = queue[0][0]
        heap = []
        res = []
        while queue or heap:
            while queue and t >= queue[0][0]:
                s, time, idx = queue.popleft()
                heapq.heappush(heap, (time, idx))
            if not heap:
                t = queue[0][0]
                continue
            cur = heapq.heappop(heap)
            t += cur[0]
            res.append(cur[1])
        return res

