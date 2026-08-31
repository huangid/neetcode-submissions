class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        target = total // k
        if max(nums) > target:
            return False
        used = [False] * len(nums)
        def backtrack(i, k, curSum):
            if k == 0:
                return True
            if curSum == target:
                return backtrack(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j] or nums[j] + curSum > target:
                    continue
                used[j] = True
                if backtrack(j+1, k, curSum + nums[j]):
                    return True
                used[j] = False
            return False
        return backtrack(0, k, 0)