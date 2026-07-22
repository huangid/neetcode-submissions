class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        m = Counter(nums)
        sort_m = sorted(m.items())
        ans = []
        for num, freq in sort_m:
            ans.extend([num] * freq)
        return ans