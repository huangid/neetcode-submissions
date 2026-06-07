class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        st = set(nums)
        s = sorted(st)
        longest = 1
        temp = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1] + 1:
                temp += 1
            else:
                longest = max(temp, longest)
                temp = 1
        longest = max(temp, longest)

        return longest