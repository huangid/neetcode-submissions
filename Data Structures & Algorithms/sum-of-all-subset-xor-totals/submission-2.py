class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)
        arr = []

        def dfs(i):
            path = 0
            nonlocal s
            if i == n:
                for a in arr:
                    path = path ^ a
                s += path
                return
            
            dfs(i+1)
            arr.append(nums[i])
            dfs(i+1)
            arr.pop()
        dfs(0)
        return s