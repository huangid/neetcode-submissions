class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0

        def dfs(i, val):
            nonlocal res
            if i == len(nums):
                res += val
                return
            
            dfs(i+1, val)
            val1 = val ^ nums[i]
            dfs(i+1, val1)
        dfs(0, 0)
        return res