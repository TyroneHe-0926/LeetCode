from collections import defaultdict

class Solution:
    def fib(self, n: int) -> int:
        nmap = defaultdict(int)
        def helper(n):
            if n == 0: return 0
            if n == 1: return 1
            if n in nmap: return nmap[n]
            nmap[n-1], nmap[n-2] = helper(n-1), helper(n-2)
            return nmap[n-1]+nmap[n-2]
        return helper(n)

solution = Solution()
print(solution.fib(2))
print(solution.fib(3))
print(solution.fib(30))