class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        maxm = self.peekMax()
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] == maxm: 
                del self.stack[i]
                return maxm

stk = MaxStack()
stk.push(5)
stk.push(1)   
stk.push(5)
print(stk.stack)
print(stk.top())     
print(stk.popMax())
print(stk.top())     
print(stk.peekMax()) 
print(stk.pop())   
print(stk.top())     