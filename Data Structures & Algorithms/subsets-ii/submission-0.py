class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        nums.sort()

        def f(i):
            if i == n:
                res.append(path.copy())
                return
            path.append(nums[i])
            f(i+1)
            path.pop()
            while i < n-1 and nums[i+1] == nums[i]:
                i += 1
            f(i+1)
        f(0)
        return res