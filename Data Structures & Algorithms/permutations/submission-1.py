class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        s = set(nums)
        path = []
        res = []
        n = len(nums)
        def dfs(i, st):
            if i == n:
                res.append(path.copy())
            for num in st:
                path.append(num)
                dfs(i+1, st-{num})
                path.pop()

        dfs(0, s)
        return res