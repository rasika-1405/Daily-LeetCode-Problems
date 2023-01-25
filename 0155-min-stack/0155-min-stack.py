class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = [inf]
        self.min_value = inf

    def push(self, val: int) -> None:
        self.min_value = min(val, self.min_value)
        self.main_stack.append(val)
        self.min_stack.append(self.min_value)

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()
        self.min_value = self.min_stack[-1]

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()