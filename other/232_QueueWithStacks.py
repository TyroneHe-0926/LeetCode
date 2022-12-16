from collections import deque

class MyQueue:
    """wtf is this"""

    queue = deque([])
    def __init__(self):
        self.queue.clear()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0