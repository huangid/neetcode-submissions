class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adjList = {i:[] for i in range(n)}
        for s, e in edges:
            adjList[s].append(e)
            adjList[e].append(s)
        visit = set()
        def dfs(i, parent):
            if i in visit:
                return False
            visit.add(i)
            for e in adjList[i]:
                if e is parent:
                    continue
                if not dfs(e, i):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n