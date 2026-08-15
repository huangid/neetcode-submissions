class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor = 0
        path = []
        def dfs(i):
            nonlocal xor
            if i == len(nums):
                s = 0
                for p in path:
                    s ^= p
                xor += s
                return
            dfs(i+1)
            path.append(nums[i])
            dfs(i+1)
            path.pop()
        dfs(0)
        return xor