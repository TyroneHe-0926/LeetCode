from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cursum, minm = 0, 0
        for num in nums:
            cursum += num
            minm = min(cursum, minm)
        return 1 if minm == 0 else abs(minm)+1