class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}

        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        
        n = len(nums)
        topK = [top for top, v in sorted(m.items(), key=lambda x: x[1])[-k:]]
        return topK