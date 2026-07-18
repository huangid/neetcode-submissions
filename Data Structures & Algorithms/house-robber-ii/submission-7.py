class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def linear(arr):
            n = len(arr)
            if n == 1:
                return arr[0]
            f = [-1] * n
            def dfs(i):
                if i >= n:
                    return 0
                if f[i] != -1:
                    return f[i]
                f[i] = max(arr[i] + dfs(i+2), dfs(i+1))
                return f[i]
            return dfs(0)
        return max(linear(nums[1:]), linear(nums[:-1]))
        
