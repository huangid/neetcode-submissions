class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        cache = {}
        def dfs(i, a, b):
            if (i, a, b) in cache:
                return cache[(i, a, b)]
            if i == len(costs):
                return 0
            cost = 1e9
            if a > 0:
                cost = costs[i][0] + dfs(i+1, a-1, b)
            if b > 0:
                cost = min(cost, costs[i][1] + dfs(i+1, a, b-1))
            cache[(i, a, b)] = cost
            return cost
        res = dfs(0, n, n)
        return res