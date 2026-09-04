class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        def time(node, parent):
            t = 0
            for c in adjList[node]:
                if c == parent:
                    continue
                childTime = time(c, node)
                if childTime or hasApple[c]:
                    t += 2 + childTime
            return t
        return time(0, -1)