from collections import defaultdict

class Solution:
    def romanToInt(self, s: str) -> int:
        m = defaultdict(int)
        result = 0
        m["I"], m["V"], m['X'], m['L'], m['C'], m['D'], m['M'] = 1, 5, 10, 50, 100, 500, 1000
        index = len(s)-1
        while index != 0:
            if m[s[index]] > m[s[index-1]] and index != 1:
                result += m[s[index]] - m[s[index-1]]
                index -= 2
            elif m[s[index]] > m[s[index-1]] and index == 1:
                result += m[s[index]] - m[s[index-1]]
                return result
            else:
                result += m[s[index]]
                index -= 1
        result += m[s[0]]
        return result


solution = Solution()
s = "III"
print(solution.romanToInt(s))
s = "LVIII"
print(solution.romanToInt(s))
s = "MCMXCIV"
print(solution.romanToInt(s))