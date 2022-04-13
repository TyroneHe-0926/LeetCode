class Solution:
    def mySqrt(self, x: int) -> int:
        count, result = 0, 1
        while result*result <= x:
            result += 1
            count += 1
        return count

solution = Solution()
print(solution.mySqrt(8))
print(solution.mySqrt(4))
print(solution.mySqrt(1))
print(solution.mySqrt(2147483647))