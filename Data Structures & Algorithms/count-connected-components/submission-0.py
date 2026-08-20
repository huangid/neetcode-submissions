class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for v in adj[i]:
                dfs(v)
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res
