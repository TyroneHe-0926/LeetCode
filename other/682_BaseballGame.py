from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for op in ops:
            if op == '+':
                s1, s2 = scores[-2:]
                scores.append(s1+s2)
            elif op == 'D': scores.append(scores[-1]*2)
            elif op == 'C': scores.pop()
            else: scores.append(int(op))
        return sum(scores)


solution = Solution()
print(solution.calPoints(["5","2","C","D","+"]))
print(solution.calPoints(ops = ["5","-2","4","C","D","9","+","+"]))
print(solution.calPoints(ops = ["1"]))