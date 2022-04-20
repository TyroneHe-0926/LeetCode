from functools import lru_cache

class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache
        def trib(n):
            if n == 0: return 0
            if n == 1 or n == 2: return 1
            return trib(n-3) + trib(n-2) + trib(n-1)
        return trib(n)