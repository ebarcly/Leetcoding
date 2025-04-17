class MinStack:

    def __init__(self):
        self.stack = []
        self.auxStack = [float('inf')] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.auxStack.append(min(val, self.auxStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.auxStack.pop()

    def top(self) -> int:
       return self.stack[-1]

    def getMin(self) -> int:
        return self.auxStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()