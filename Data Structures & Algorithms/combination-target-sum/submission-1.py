class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)

        def f(i, t):
            if t == 0:
                res.append(path.copy())
                return
            if t < 0 or i == n:
                return
            path.append(nums[i])
            f(i, t-nums[i])
            path.pop()
            f(i+1, t)
        f(0, target)
        return res