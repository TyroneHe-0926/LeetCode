from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            cur = ""
            if not i % 3: cur += "Fizz"
            if not i % 5: cur += "Buzz"
            if not cur: cur = str(i)
            result.append(cur)
        return result

solution = Solution()
print(solution.fizzBuzz(3))
print(solution.fizzBuzz(5))
print(solution.fizzBuzz(15))