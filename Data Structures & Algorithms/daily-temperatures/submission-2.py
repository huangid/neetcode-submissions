class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        length = len(temperatures)
        for i, t in enumerate(temperatures):
            j = i + 1
            while j < length and temperatures[j] <= t:
                j += 1
            if j != length:
                result.append(j-i)
            else:
                result.append(0)
        return result