class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        path = []
        res = 0
        n = len(nums)
        def dfs(i):
            nonlocal res
            if i >= n:
                xor = 0
                for num in path:
                    xor = xor ^ num
                res += xor
                return
            dfs(i+1)
            path.append(nums[i])
            dfs(i+1)
            path.pop()
        dfs(0)
        return res