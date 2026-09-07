class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p1 = p2 = 0
        while True:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break
        p3 = 0
        while True:
            p2 = nums[p2]
            p3 = nums[p3]
            if p2 == p3:
                return p2
