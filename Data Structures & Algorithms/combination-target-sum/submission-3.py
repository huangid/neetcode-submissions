class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        n = len(nums)

        def dfs(i):
            if i == n and sum(path) == target:
                res.append(path.copy())
                return
            if i == n or sum(path) > target:
                return
            
            dfs(i+1)
            path.append(nums[i])
            dfs(i)
            path.pop()
        dfs(0)
        return res