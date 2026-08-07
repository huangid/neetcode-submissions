class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s = 0
        arr = []
        n = len(nums)
        def dfs(i):
            path = 0
            for a in arr:
                path = path ^ a
            nonlocal s
            s += path
            if i == n:
                return
            for j in range(i, n):
                arr.append(nums[j])
                dfs(j+1)
                arr.pop()
        dfs(0)
        return s