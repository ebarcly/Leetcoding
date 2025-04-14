class MinStack:

    def __init__(self):
        self.stack = []
        self.auxStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.auxStack or val <= self.auxStack[-1]:
            self.auxStack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.auxStack[-1]:
            self.auxStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.auxStack:
            return self.auxStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
