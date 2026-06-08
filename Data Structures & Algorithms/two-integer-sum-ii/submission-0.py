class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = defaultdict(int)
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in m:
                return [m[diff]+1, i+1]
            m[num] = i
        
