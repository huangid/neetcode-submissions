class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        l = len(nums)
        for num in nums:
            m[num] = m.get(num, 0) + 1
            if m[num] > l // 2:
                return num
