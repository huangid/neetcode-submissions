class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums) // 3
        counter = Counter(nums)
        for num, freq in counter.items():
            if freq > n:
                res.append(num)
        return res