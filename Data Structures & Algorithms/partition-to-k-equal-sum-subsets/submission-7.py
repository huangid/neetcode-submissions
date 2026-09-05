class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        ave = total // k
        if max(nums) > ave:
            return False
        used = [False] * len(nums)
        def dfs(i, k, curSum):
            if k == 0:
                return True
            if curSum == ave:
                return dfs(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j] or nums[j] + curSum > ave:
                    continue
                used[j] = True
                if dfs(j+1, k, curSum + nums[j]):
                    return True
                used[j] = False
            return False
        return dfs(0, k, 0)
                
