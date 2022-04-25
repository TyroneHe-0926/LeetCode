from typing import List


class Solution():
    """LC generate all possible permutations of parenthesis"""
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

class Solution():
    def generateParenthesis(self, n):
        self.result = []
        def generate(parens: List, left, right):
            if len(parens) == 2*n: self.result.append("".join(parens))
            else:
                if left < n:
                    parens.append('(')
                    generate(parens, left+1, right)
                    parens.pop()
                if right < left:
                    parens.append(')')
                    generate(parens, left, right+1)
                    parens.pop()
        generate([], 0, 0)
        return self.result

solution = Solution()
print(solution.generateParenthesis(3))
# solution.generateParenthesis()