from collections import defaultdict

class Solution:
    def originalDigits(self, s: str) -> str:
        cmap = defaultdict(int)
        digits = []
        for char in s:
            cmap[char] += 1

        while cmap['w']:
            digits.append(2)
            cmap['w'] -= 1
            cmap['t'] -= 1
            cmap['o'] -= 1
            
        while cmap['u']:
            digits.append(4)
            cmap['f'] -= 1
            cmap['o'] -= 1
            cmap['u'] -= 1
            cmap['r'] -= 1
        
        while cmap['x']:
            digits.append(6)
            cmap['s'] -= 1
            cmap['i'] -= 1
            cmap['x'] -= 1
        
        while cmap['g']:
            digits.append(8)
            cmap['g'] -= 1
            cmap['h'] -= 1
            cmap['e'] -= 1
            cmap['i'] -= 1
            cmap['t'] -= 1
        
        while cmap['z']:
            digits.append(0)
            cmap['z'] -= 1
            cmap['e'] -= 1
            cmap['r'] -= 1
            cmap['o'] -= 1

        while cmap['o']:
            digits.append(1)
            cmap['o'] -= 1
            cmap['n'] -= 1
            cmap['e'] -= 1

        while cmap['h']:
            digits.append(3)
            cmap['t'] -= 1
            cmap['h'] -= 1
            cmap['r'] -= 1
            cmap['e'] -= 2

        while cmap['s']:
            digits.append(7)
            cmap['s'] -= 1
            cmap['e'] -= 2
            cmap['v'] -= 1
            cmap['n'] -= 1
        
        while cmap['f']:
            digits.append(5)
            cmap['f'] -= 1
            cmap['i'] -= 1
            cmap['v'] -= 1
            cmap['e'] -= 1
        
        while cmap['n']:
            digits.append(9)
            cmap['n'] -= 2
            cmap['i'] -= 1
            cmap['e'] -= 1
        
        return "".join([str(i) for i in sorted(digits)])


solution = Solution()
print(solution.originalDigits(s = "owoztneoer"))
print(solution.originalDigits(s = "fviefuro"))