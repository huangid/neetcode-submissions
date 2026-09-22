class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        def dfs(i, cur):
            if cur == target:
                res.append(path.copy())
                return
            if i == len(nums) or cur > target:
                return
            path.append(nums[i])
            dfs(i, cur + nums[i])
            path.pop()
            dfs(i+1, cur)
        dfs(0, 0)
        return res
