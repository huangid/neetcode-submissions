class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course = {i:[] for i in range(numCourses)}
        for crs in prerequisites:
            course[crs[0]].append(crs[1])
        res = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for c in course[crs]:
                if not dfs(c):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        
