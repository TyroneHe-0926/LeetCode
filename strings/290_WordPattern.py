from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        pmap = defaultdict(str)
        marked = set()

        if len(pattern) != len(s): return False
        
        for index, char in enumerate(pattern):
            if char not in pmap:
                if s[index] not in marked:
                    pmap[char] = s[index]
                    marked.add(s[index])
                else:
                    return False
            else:
                if pmap[char] != s[index]: return False
        
        return True
