class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()
        n = len(candidates)
        def dfs(i, cursum):
            if cursum == target:
                res.append(path.copy())
                return
            if i == n or cursum > target:
                return
            path.append(candidates[i])
            dfs(i+1, cursum+candidates[i])
            path.pop()
            while i + 1 < n and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cursum)
        dfs(0, 0)
        return res