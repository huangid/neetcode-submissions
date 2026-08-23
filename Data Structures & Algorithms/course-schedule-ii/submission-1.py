class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course = {i:[] for i in range(numCourses)}
        for crs in prerequisites:
            course[crs[0]].append(crs[1])
        res = []
        visit = set()
        seen = set()
        def dfs(crs):
            if crs in visit:
                return True
            if crs in seen:
                return False
            seen.add(crs)
            for c in course[crs]:
                if not dfs(c):
                    return False
            res.append(crs)
            seen.remove(crs)
            visit.add(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
