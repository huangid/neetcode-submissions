class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQ = deque()
        minQ = deque()
        l = 0
        res = 0
        for r in range(len(nums)):
            while minQ and nums[r] <= minQ[-1][1]:
                minQ.pop()
            minQ.append((r, nums[r]))
            while maxQ and nums[r] >= maxQ[-1][1]:
                maxQ.pop()
            maxQ.append((r, nums[r]))
            while abs(minQ[0][1] - maxQ[0][1]) > limit:
                if minQ[0][0] == l:
                    minQ.popleft()
                elif maxQ[0][0] == l:
                    maxQ.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res