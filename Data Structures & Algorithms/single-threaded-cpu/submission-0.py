class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i) # enqueue time, process time, index
        tasks.sort(key=lambda t:t[0])
        heap = []
        res = []
        time = tasks[0][0]
        i = 0
        while i < len(tasks) or heap:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not heap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(heap)
                time += procTime
                res.append(index)

        return res