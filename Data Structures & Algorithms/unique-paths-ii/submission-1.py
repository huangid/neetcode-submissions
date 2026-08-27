class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(w+1)] for _ in range(h+1)]
        if obstacleGrid[h-1][w-1] == 1:
            return 0
        dp[h-1][w-1] = 1
        for i in range(h-1, -1, -1):
            for j in range(w-1, -1, -1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] += dp[i+1][j] + dp[i][j+1]
        return dp[0][0]