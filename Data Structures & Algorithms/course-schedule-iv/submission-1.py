class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[b].append(a)
        cache = {}
        def dfs(u, v):
            if (u, v) in cache:
                return cache[(u, v)]
            prereq = False
            if not adj[v]:
                prereq = False
            elif u in adj[v]:
                prereq = True
            else:
                for p in adj[v]:
                    if dfs(u, p):
                        prereq = True
            cache[(u, v)] = prereq
            return prereq
        res = []
        for u, v in queries:
            res.append(dfs(u, v))
        return res