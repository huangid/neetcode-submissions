class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(candidates)
        candidates.sort()

        def f(i, t):
            if t == 0:
                res.append(path.copy())
                return
            if t < 0 or i == n:
                return
            path.append(candidates[i])
            f(i+1, t-candidates[i])
            path.pop()
            while i < n-1 and candidates[i+1] == candidates[i]:
                i += 1
            f(i+1, t)
        f(0, target)
        return res