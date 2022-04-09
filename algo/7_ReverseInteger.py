class Solution:
    def reverse(self, x: int) -> int:
        rev = 0;
        while x != 0:
            pop = int(x % 10);
            x //= 10;
            if rev > 2147483647/10 or (rev == 2147483647 / 10 and pop > 7): return 0
            if rev < -2147483648/10 or (rev == -2147483648 / 10 and pop < -8): return 0
            rev = rev * 10 + pop;
        return rev;


solution = Solution()
x = 123
print(solution.reverse(x))
x = -123
print(solution.reverse(x))
x = 120
print(solution.reverse(x))

"""
Cheese
class Solution:
    def reverse(self, x: int) -> int:
        xstr = str(x)[::-1] if not x < 0 else str(x)[1:][::-1]
        xstr = xstr.lstrip("0") if len(xstr) > 1 else xstr
        xint = int("-"+xstr) if x < 0 else int(xstr)
        return xint if xint >= -2147483648 and xint <= 2147483647 else 0
"""