from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        fmap = defaultdict(int)
        for c in s: fmap[c] += 1

        fmap = dict(sorted(fmap.items(), key=lambda x: x[1], reverse=True))
        res = ""
        for k,v in fmap.items():
            for i in range(v): res += k
        
        return res

s = Solution()
s.frequencySort("cccaaa")
s.frequencySort("tree")