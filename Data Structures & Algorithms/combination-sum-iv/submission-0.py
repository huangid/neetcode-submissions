class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(curSum):
            if curSum == target:
                return 1
            elif curSum > target:
                return 0
            if curSum in cache:
                return cache[curSum]
            cache[curSum] = sum(dfs(curSum+n) for n in nums)
            return cache[curSum]
        return dfs(0)