class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def f(i, cur, total):
            
            if total == target:
                res.append(cur.copy())
                return
            if i == len(candidates) or total > target:
                return
            cur.append(candidates[i])
            f(i+1, cur, total+candidates[i])
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            f(i+1, cur, total)

        f(0, [], 0)
        return res
