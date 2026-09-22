class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start = []
        pre = 0
        for arr, time in customers:
            st = max(pre, arr)
            start.append(st)
            pre = st + time
        total = 0
        for i, cus in enumerate(customers):
            wait = start[i] + cus[1] - cus[0]
            total += wait

        return total / len(customers)
