class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(i, par):
            time = 0
            for a in adj[i]:
                if a == par:
                    continue
                child = dfs(a, i)
                if hasApple[a] or child > 0:
                    time += 2 + child
            return time
        return dfs(0, -1)