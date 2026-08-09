class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k:
            return False
        part = s / k
        if max(nums) > part:
            return False
        arr = [0] * k
        nums.sort(reverse=True)
        def dfs(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if arr[j] + nums[i] <= part:
                    arr[j] += nums[i]
                    if dfs(i+1):
                        return True
                    arr[j] -= nums[i]
                if arr[j] == 0:
                    break
            return False
        return dfs(0)
