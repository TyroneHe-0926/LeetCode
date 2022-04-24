from collections import defaultdict

class Logger:

    def __init__(self):
        self.log = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.log: 
            self.log[message] = timestamp + 10
            return True
        if message in self.log and self.log[message] > timestamp: return False
        elif message in self.log and self.log[message] <= timestamp: 
            self.log[message] = timestamp + 10
            return True