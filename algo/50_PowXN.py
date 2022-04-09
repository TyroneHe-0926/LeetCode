class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x: float, n: int):
            if n == 0:
                return 1
            half = round(fastPow(x, n//2), 50)
            if n % 2 == 0:
                return round(half * half, 50)
            else:
                return round(half * half * x, 50)
        return round(fastPow(x, n),5) if n > 0 else round(1/fastPow(x,abs(n)), 5)


class SolutionIter:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1: # same as if n % 2 != 0
                pow *= x
            x *= x
            n >>= 1 # same as n //= 2
        return pow

class SolutionRecur:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
            

solution = Solution()
print(solution.myPow(x = 8.88023, n = 3))
print(solution.myPow(x = 0.00001, n = 2147483647))
print(solution.myPow(x = 0.25519, n = -6))