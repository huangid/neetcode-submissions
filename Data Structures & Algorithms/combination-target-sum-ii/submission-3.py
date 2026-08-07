class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()

        def dfs(i, t):
            if t == 0:
                res.append(path.copy())
                return
            if t < 0 or i >= len(candidates):
                return
            
            path.append(candidates[i])
            dfs(i+1, t-candidates[i])
            path.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, t)
        dfs(0, target)
        return res
