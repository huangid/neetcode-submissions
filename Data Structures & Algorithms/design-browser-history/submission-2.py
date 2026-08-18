class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = []
        self.arr.append(homepage)
        self.i = 0

    def visit(self, url: str) -> None:
        self.i += 1
        self.arr = self.arr[:self.i]
        self.arr.append(url)

    def back(self, steps: int) -> str:
        if self.i >= steps:
            self.i -= steps
        else:
            self.i = 0
        return self.arr[self.i]

    def forward(self, steps: int) -> str:
        while steps and self.i < len(self.arr) - 1:
            self.i += 1
            steps -= 1
        return self.arr[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)