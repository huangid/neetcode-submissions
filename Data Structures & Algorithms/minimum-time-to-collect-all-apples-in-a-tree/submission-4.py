class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        cache = {}
        def time(node, parent):
            if (node, parent) in cache:
                return cache[(node, parent)]
            t = 0
            for c in adjList[node]:
                if c == parent:
                    continue
                if hasApple[c] or time(c, node):
                    t += 2 + time(c, node)
            cache[(node, parent)] = t
            return t
        return time(0, -1)