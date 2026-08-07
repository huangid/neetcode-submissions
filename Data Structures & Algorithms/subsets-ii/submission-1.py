class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        path = []
        res = []
        nums.sort()
        def dfs(i):
            res.append(path.copy())
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                if i < j:
                    if nums[j] == nums[j-1]:
                        continue
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return res