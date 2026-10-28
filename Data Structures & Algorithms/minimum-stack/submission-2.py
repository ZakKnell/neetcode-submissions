class MinStack:

    def __init__(self):
        self.minStack = [] # [val, currentMin]

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append([val, val])
        else:
            if self.minStack[-1][1] < val:
                self.minStack.append([val, self.minStack[-1][1]])
            else:
                self.minStack.append([val, val])

    def pop(self) -> None:
        self.minStack.pop()

    def top(self) -> int:
        return self.minStack[-1][0]

    def getMin(self) -> int:
        return int(self.minStack[-1][1])