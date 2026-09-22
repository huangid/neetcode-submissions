class StockSpanner:

    def __init__(self):
        self.stack = [] 

    def next(self, price: int) -> int:
        day = 1
        while self.stack and price >= self.stack[-1][0]:
            p, d = self.stack.pop()
            day += d
        self.stack.append([price, day])
        return day


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)