class Solution:
    def myAtoi(self, s: str) -> int:
        myint, negative = "", False
        # 1. remove leading whitesapce
        s = s.lstrip()
        if not s: return 0

        # 2. check for sign
        if s[0] == '-':
            negative = True
            s = s[1:]
        elif s[0] == '+': s = s[1:]

        # 3. remove leading 0s
        s = s.lstrip('0')
        
        for c in s:
            if c.isdigit(): myint += c
            else: break
        
        if not myint: return 0

        myint = int(myint)
        if not negative and myint > 2147483647: myint = 2147483647
        if negative and myint > 2147483648: myint = 2147483648

        return 0 - myint if negative else myint

solution = Solution()
# print(solution.myAtoi("42"))
# print(solution.myAtoi("    -42"))
# print(solution.myAtoi("  +4 2"))
# print(solution.myAtoi("0032"))
# print(solution.myAtoi("--32"))
# print(solution.myAtoi("32 with words"))
print(solution.myAtoi("00-32")) #0