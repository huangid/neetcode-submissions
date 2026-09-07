class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        curnum = 0
        maxnum = 0
        for i in range(n):
            if i < minutes:
                if grumpy[i] == 1:
                    curnum += customers[i]
                    maxnum = curnum
            else:
                if grumpy[i] == 1:
                    curnum += customers[i]
                if grumpy[i-minutes] == 1:
                    curnum -= customers[i-minutes]
                maxnum = max(maxnum, curnum)
        for c, g in zip(customers, grumpy):
            if g == 0:
                maxnum += c
        return maxnum