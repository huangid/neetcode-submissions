class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for i in range(len(costs)):
            diff.append((costs[i][0] - costs[i][1], i))
        diff.sort()
        total = 0
        n = len(costs) // 2
        for i in range(n):
            total += costs[diff[i][1]][0]
            total += costs[diff[i+n][1]][1]
        return total
        