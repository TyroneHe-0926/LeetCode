from collections import defaultdict
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        fmap, l, tsum = defaultdict(int), len(arr)//2, 0
        res = set()
        for num in arr: fmap[num] += 1
        fmap = {k: v for k, v in sorted(fmap.items(), key=lambda item: item[1], reverse=True)}
        for k, v in fmap.items():
            tsum += v
            res.add(k)
            if tsum >= l: return len(res)

s = Solution()
arr = [3,3,3,3,5,5,5,2,2,7]
print(s.minSetSize(arr))