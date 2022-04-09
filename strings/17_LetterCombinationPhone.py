from typing import List
from collections import defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        lmap = defaultdict(list)
        lmap['2'],lmap['3'],lmap['4'],lmap['5'],lmap['6'],lmap['7'],lmap['8'],lmap['9'] = ['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']
        results = [char for char in lmap[digits[0]]]
        digits = digits[1:]

        while digits:
            base_digit = digits[0]
            digits = digits[1:]
            results = [result+c for result in results for c in lmap[base_digit]]
        
        return results

from collections import deque
class Solution:
    """Deque BFS"""
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {1: '', 2: 'abc',3: 'def',4: 'ghi',5: 'jkl',6: 'mno',7: 'pqrs',8: 'tuv',9: 'wxyz'}
        q = deque(d[int(digits[0])])
        
        for i in range(1,len(digits)):
            s = len(q)
            while s:
                out = q.popleft()
                for j in d[int(digits[i])]:
                    q.append(out + j)
                s -= 1
                
        return q

solution = Solution()
print(solution.letterCombinations(digits = "2345"))
print(solution.letterCombinations(digits = ""))
print(solution.letterCombinations(digits = "2"))