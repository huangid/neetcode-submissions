class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        self.stack2.append(x)
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        pop = self.stack1.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return pop

    def peek(self) -> int:
        return self.stack1[0]
        
    def empty(self) -> bool:
        return not self.stack1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()