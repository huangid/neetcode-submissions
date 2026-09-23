class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def time(i, par):
            t = 0
            for c in adj[i]:
                if c == par:
                    continue
                childTime = time(c, i)
                if hasApple[c] or childTime > 0:
                    t += (childTime + 2)
            return t
        return time(0, -1)
        