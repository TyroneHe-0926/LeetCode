from typing import List
from collections import defaultdict
class Solution:
    def expand(self, s: str) -> List[str]:
        ans = [""]
        for z in s.replace("{", " ").replace("}", " ").split():
            ans = [x + y for x in ans for y in sorted(z.split(","))]
                
        return ans

class Solution:
    def expand(self, s: str) -> List[str]:
        selections, individuals, selecting, selectindex = defaultdict(list), defaultdict(int), False, -1
        for index, char in enumerate(s):
            if selecting and char != "," and char != "}": 
                selections[selectindex].append(char)
                continue
            if char == "{": 
                selecting, selectindex = True, index
                continue
            if char == "}": 
                selecting = False
                continue
            if char.isalpha(): individuals[index] = char
        
        results = []
        for i in range(len(s)):
            if i in individuals:
                results = [result+individuals[i] for result in results] if results else [individuals[i]]
            if i in selections:
                results = [result+astr for result in results for astr in selections[i]] if results else [astr for astr in selections[i]]
        
        results.sort()
        return results

solution = Solution()
print(solution.expand(s = "{a,b}c{d,e}f"))
print(solution.expand(s = "abcd"))
print(solution.expand(s = "a{b,c}"))