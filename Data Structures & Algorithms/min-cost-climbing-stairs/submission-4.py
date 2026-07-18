class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1 = cost[1]
        prev2 = cost[0]

        for i in range(2, len(cost)):
            cur = min(prev1, prev2) + cost[i]
            prev1, prev2 = cur, prev1
        return min(prev1, prev2)