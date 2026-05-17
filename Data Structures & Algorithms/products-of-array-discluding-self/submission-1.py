class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        suf = [0] * n

        pre[0] = 1
        suf[-1] = 1
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]

        prod = [0] * n
        for i in range(n):
            prod[i] = pre[i] * suf[i]

        return prod
