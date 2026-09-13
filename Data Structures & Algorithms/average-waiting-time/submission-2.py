class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        prev = 0
        for arr, time in customers:
            if arr >= prev:
                total += time
                prev = arr + time
            else:
                total += time + prev - arr
                prev = prev + time
        return total / len(customers)
            