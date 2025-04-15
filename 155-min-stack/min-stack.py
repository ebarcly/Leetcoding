class MinStack:

    def __init__(self):
        self.main = []
        self.auxStack = [float('inf')]  

    def push(self, val: int) -> None:
        self.main.append(val)
        self.auxStack.append(min(val, self.auxStack[-1]))

    def pop(self) -> None:
        self.main.pop()
        self.auxStack.pop()

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.auxStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()