class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i in range(k):
            if nums[i] in s:
                return True
            s.add(nums[i])
        for i in range(len(nums)-k):
            j = i + k
            if nums[j] in s:
                return True
            s.add(nums[j])
            s.remove(nums[i])
        return False
