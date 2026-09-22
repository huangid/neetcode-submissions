class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            adjList[a].append(b)
        cycle = set()
        visit = set()
        def search(i):
            if i in visit:
                return True
            if i in cycle:
                return False
            cycle.add(i)
            for p in adjList[i]:
                if not search(p):
                    return False
            cycle.remove(i)
            visit.add(i)
            return True
        for i in range(numCourses):
            if not search(i):
                return False
        return True
