class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        date = []
        length = len(temperatures)
        for i, t in enumerate(temperatures):
            j = i + 1
            while j < length and temperatures[j] <= t:
                j += 1
            if j != length:
                date.append(j-i)
            else:
                date.append(0)
        return date