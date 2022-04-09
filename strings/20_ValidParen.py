from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        match = deque([])
        closing = ")]}"
        for char in s:
            if char == "(":
                match.appendleft(")")
            elif char == "[":
                match.appendleft("]")
            elif char == "{":
                match.appendleft("}")
            
            if char in closing and len(match) == 0:
                return False
            elif char in closing and match[0] != char:
                return False
            elif char in closing and match[0] == char:
                match.popleft()
            
        return len(match) == 0


solution = Solution()
s = ")"
print(solution.isValid(s))
s = "()[]{}"
print(solution.isValid(s))
s = "(]"
print(solution.isValid(s))
s = "([)]"
print(solution.isValid(s))
s = "(([[()]]))"
print(solution.isValid(s))