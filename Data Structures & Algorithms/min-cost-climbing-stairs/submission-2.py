class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        f = [-1] * len(cost)
        def dfs(i):
            if i >= len(cost):
                return 0
            if f[i] is not -1:
                return f[i]
            f[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return f[i]
        return min(dfs(0), dfs(1))