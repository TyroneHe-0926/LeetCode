from typing import List
from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nmap, flipped = defaultdict(int), defaultdict(list)
        for i in arr: nmap[i]+=1
        for key, value in nmap.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                flipped[value].append(key)
        
        for key, value in flipped.items():
            if len(value) > 1: return False
        
        return True
        

solution = Solution()
print(solution.uniqueOccurrences(arr = [1,2,2,1,1,3]))
print(solution.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))
print(solution.uniqueOccurrences(arr=[1,2]))