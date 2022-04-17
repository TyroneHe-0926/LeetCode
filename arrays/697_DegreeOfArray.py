from typing import List
from collections import defaultdict
import math

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nmap = defaultdict(dict)
        for index, num in enumerate(nums):
            if num not in nmap:
                nmap[num]["freq"] = 1
                nmap[num]["start"] = index
                nmap[num]["end"] = index
            else:
                nmap[num]["freq"] += 1
                nmap[num]["end"] = index
        nmap = dict(sorted(nmap.items(), key=lambda x: x[1]["freq"], reverse=True))
        maxfreq, occur = 0, math.inf 
        for num, ninfo in nmap.items():
            freq, length = ninfo["freq"], ninfo["end"] - ninfo["start"] + 1
            if freq >= maxfreq and length < occur:
                maxfreq, occur = freq, length
        return occur

solution = Solution()
print(solution.findShortestSubArray(nums = [1,2,2,3,1]))
print(solution.findShortestSubArray(nums = [1,2,2,3,1,4,2]))
print(solution.findShortestSubArray([1]))