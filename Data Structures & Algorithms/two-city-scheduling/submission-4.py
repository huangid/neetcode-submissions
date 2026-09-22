class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for i, c in enumerate(costs):
            diff.append((c[0]-c[1], i))
        diff.sort()
        total = 0
        n = len(costs)//2
        for i in range(n):
            total += costs[diff[i][1]][0]
            total += costs[diff[i+n][1]][1]
        return total