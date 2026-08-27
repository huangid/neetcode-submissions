class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}
        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in cache:
                return cache[(i, m, n)]
            mCnt, nCnt = strs[i].count("0"), strs[i].count("1")
            cache[(i, m, n)] = dfs(i+1, m, n)
            if m >= mCnt and n >= nCnt:
                cache[(i, m, n)] = max(cache[(i, m, n)], 1 + dfs(i+1, m-mCnt, n-nCnt))
            return cache[(i, m, n)]
        return dfs(0, m, n)