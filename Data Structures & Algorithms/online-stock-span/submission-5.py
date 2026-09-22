class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
            return 1
        else:
            num = 1
            while self.stack and self.stack[-1][0] <= price:
                p, n = self.stack.pop()
                num += n
            self.stack.append((price, num))
            return num

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)