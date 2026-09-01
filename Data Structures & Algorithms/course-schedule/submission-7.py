class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            adjList[a].append(b)
        visit = set()
        def dfs(cls, seen):
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