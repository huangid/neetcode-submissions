class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.i += 1
        self.stack = self.stack[:self.i]
        self.stack.append(url)

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.i != 0:
                self.i -= 1
        return self.stack[self.i]

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.i != len(self.stack) - 1:
                self.i += 1
        return self.stack[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)