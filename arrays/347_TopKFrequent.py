from typing import List
from collections import defaultdict
import heapq

class Solution:
    """O(nlogk) with heap O(n) for map, O(logk) for heap push"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap, freqs = defaultdict(int), []
        for num in nums: freqmap[num] += 1
        for i in freqmap:
            heapq.heappush(freqs, (freqmap[i], i))
        return [num for _, num in heapq.nlargest(k, freqs)]
        

solution = Solution()
print(solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(solution.topKFrequent(nums = [1], k = 1))