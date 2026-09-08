import sys
sys.setrecursionlimit(200000)
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        l = len(s)
        cache = {}
        def dfs(i):
            if i == l - 1:
                return True
            if i in cache:
                return cache[i]
            res = False
            for j in range(i+minJump, min(i+maxJump, l-1) + 1):
                if s[j] == '0' and dfs(j):
                    res = True
                    break
            cache[i] = res
            return res
        return dfs(0)