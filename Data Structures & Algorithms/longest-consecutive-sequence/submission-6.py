class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:
                long = 1
                num += 1
                while num in s:
                    num += 1
                    long += 1

                longest = max(long, longest)

        return longest       