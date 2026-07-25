class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        for i in range(n-1):
            end = i+1+k if i+1+k < n else n
            for j in range(i+1, end):
                if nums[i] == nums[j]:
                    return True
        return False