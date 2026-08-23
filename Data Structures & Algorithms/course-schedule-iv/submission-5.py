class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        cache = {}
        for a, b in prerequisites:
            adj[b].append(a)
        def dfs(u, v):
            if (u, v) in cache:
                return cache[(u, v)]
            if u in adj[v]:
                cache[(u, v)] = True
                return True
            for p in adj[v]:
                if dfs(u, p):
                    cache[(u, v)] = True
                    return True
            cache[(u, v)] = False
            return False
        res = []
        for u, v in queries:
            res.append(dfs(u, v))
        return res
