from typing import List
from collections import defaultdict

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordermap = defaultdict(int)
        for i, c in enumerate(order): ordermap[c] = i
        last = self.turn(words[0], ordermap)
        for word in words[1:]:
            cur =  self.turn(word, ordermap)
            if not self.check(last, cur): return False
            last = cur
        return True
    
    def turn(self, word, ordermap):
        return [ordermap[c] for c in word]
    
    def check(self, l1, l2):
        """Check if l2 is lexo bigger or equal to l1"""
        for l1c, l2c in zip(l1, l2):
            if l2c > l1c: return True
            elif l2c < l1c: return False
            else: continue
        return True if len(l2) >= len(l1) else False

solution = Solution()
print(solution.isAlienSorted(["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"))