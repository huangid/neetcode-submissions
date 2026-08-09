class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        fourside = sum(matchsticks)
        if fourside%4 != 0:
            return False
        side = fourside / 4
        
        if max(matchsticks) > side:
            return False
        
        arr = [0] * 4 # 4 side
        
        def dfs(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if arr[j] + matchsticks[i] <= side:
                    arr[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    arr[j] -= matchsticks[i]
            return False

        return dfs(0)