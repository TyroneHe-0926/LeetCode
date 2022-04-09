from typing import List
from functools import reduce
#key to this question is actually to go from right to left to avoid length delta ...

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        slist = list(s)
        ist = sorted(list(zip(indices, sources, targets)), key=lambda x: x[0], reverse=True)
        for x in ist:
            indice, src, target = x[0], x[1], x[2]
            seg = s[indice:indice+len(src)]
            if seg == src:
                slist[indice:indice+len(src)] = target
"""
1 line on leetcode
return reduce(lambda S, (i, s, t): S[:i] + t + S[i + len(s):] if S[i:i + len(s)] == s else S, sorted(zip(indexes, sources, targets))[::-1], S)
"""

        

solution = Solution()
s,indices,sources,targets = "abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]
print(solution.findReplaceString(s,indices,sources, targets))
s,indices,sources,targets = "abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]
print(solution.findReplaceString(s,indices,sources, targets))
s,indices,sources,targets = "vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]
print(solution.findReplaceString(s,indices,sources, targets))