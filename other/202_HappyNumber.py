class Solution:
    def isHappy(self, n: int) -> bool:
        seen, nstr = set(), str(n)
        while True:
            result = self.get_sum(nstr)
            if result in seen: return False
            if result == 1: return True
            seen.add(result)
            nstr = str(result)
    
    def get_sum(self, n):
        result = 0
        for c in n: result+=int(c)**2
        return result

solution = Solution()
print(solution.isHappy(1923))
print(solution.isHappy(2))