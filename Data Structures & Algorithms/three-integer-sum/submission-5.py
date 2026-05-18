class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        threeSum = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            newTarget = -nums[i]
            twoSum = self.twoSum(nums[i+1:], newTarget)
            for sd, td in twoSum:
                threeSum.append([nums[i], sd, td])
        return threeSum

    def twoSum(self, nums, target):
        l = 0
        r = len(nums) - 1
        twoSum = []
        while l < r:
            sum = nums[l] + nums[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                twoSum.append((nums[l], nums[r]))
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
        return twoSum