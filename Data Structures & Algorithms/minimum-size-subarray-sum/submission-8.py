class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cursum = 0
        mLen = 1e9
        for r in range(len(nums)):
            cursum += nums[r]
            while cursum >= target:
                mLen = min(mLen, r - l + 1)
                cursum -= nums[l]
                l += 1
        return mLen if mLen < 1e9 else 0
            