class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for a, b in prerequisites:
            if a not in adjList:
                adjList[a] = []
            if b not in adjList:
                adjList[b] = []
            adjList[a].append(b)
        visit = set()
        def dfs(cls, seen):
            seen.add(cls)
            if cls in visit:
                return True
            for c in adjList[cls]:
                if c in seen:
                    return False
                seen.add(c)
                if not dfs(c, seen):
                    return False
                seen.remove(c)
            visit.add(cls)
            return True
        
        for cls in adjList:
            if not dfs(cls, set()):
                return False
        return True