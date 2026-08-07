class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        path = []
        res = []

        def dfs(i):
            if len(path) == k:
                res.append(path.copy())
                return
            
            for num in range(i, n+1):
                path.append(num)
                dfs(num+1)
                path.pop()

        dfs(1)
        return res
