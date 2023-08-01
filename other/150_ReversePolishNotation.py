from collections import deque
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque([])
        for token in tokens:
            if token.lstrip("-").isdigit(): stack.append(token)
            else:
                d1 = int(stack.pop())
                d2 = int(stack.pop())

                result = 0

                if token == '+': result = d2+d1
                if token == '-': result = d2-d1
                if token == '/': result = d2/d1
                if token == '*': result = d2*d1

                stack.append(int(result))
        
        return int(stack[-1])
        

s = Solution()
# s.evalRPN(tokens = ["2","1","+","3","*"])
# s.evalRPN(tokens = ["4","13","5","/","+"])
# s.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
s.evalRPN(["18"])