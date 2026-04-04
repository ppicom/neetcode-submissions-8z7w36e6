class MyStack:

    def __init__(self):
        self.queue = []
        self.size = 0
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return -1

        for _ in range(self.size -1):
            f = self.queue.pop(0)
            self.queue.append(f)
        
        self.size -= 1
        return self.queue.pop(0)

    def top(self) -> int:
        if self.empty():
            return -1
        e = self.pop()
        self.queue.append(e)
        self.size += 1 # to compensate for reusing pop()
        return e

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()