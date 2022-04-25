from typing import List
from collections import defaultdict

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1: return 0
        fmap, bmap = defaultdict(int), defaultdict(int)
        fmap[0], bmap[length-1] = 0, 0
        for i in range(1, length): fmap[i] = fmap[i-1] + nums[i-1]
        for i in range(length-2, -1, -1): bmap[i] = bmap[i+1] + nums[i+1]
        for index, num in fmap.items():
            if bmap[index] == num: return index
        return -1

class Solution():
    """O(1) space"""
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

solution = Solution()
print(solution.pivotIndex(nums = [1,7,3,6,5,6]))
print(solution.pivotIndex(nums = [1,2,3]))
print(solution.pivotIndex(nums = [2,1,-1]))