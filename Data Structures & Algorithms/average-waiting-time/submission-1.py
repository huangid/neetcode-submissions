class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        pre = 0
        wait = 0
        for s, t in customers:
            start = max(s, pre)
            wait += start + t - s
            pre = start + t
        return wait / len(customers)