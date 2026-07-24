class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            while j < n - 2:
                k = j + 1
                z = n - 1
                while k < z:
                    if nums[i]+nums[j]+nums[k]+nums[z] < target:
                        k += 1
                    elif nums[i]+nums[j]+nums[k]+nums[z] > target:
                        z -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[z]])
                        k += 1
                        z -= 1
                        while k < z and nums[k] == nums[k-1]:
                            k += 1
                        while k < z and nums[z] == nums[z+1]:
                            z -= 1
                j += 1
                while j < n - 2 and nums[j] == nums[j-1]:
                    j += 1
            while i < n - 3 and nums[i] == nums[i-1]:
                i += 1

        return res
                        
                    