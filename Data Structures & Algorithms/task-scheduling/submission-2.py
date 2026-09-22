class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        for freq in count.values():
            heap.append(freq)
        
        heap.sort()
        maxi = heap[-1]
        time = (n+1) * (maxi-1)
        for i in range(len(heap)):
            heap[i] = heap[i]-maxi
            if heap[i] >= 0:
                time += 1

        return max(len(tasks), time)
