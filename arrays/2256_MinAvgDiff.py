import random
from typing import List
from collections import defaultdict
import math

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        fmap, bmap = defaultdict(int), defaultdict(int)
        length = len(nums)

        #forward index mapped to prefix sum
        temp = 0
        for index, num in enumerate(nums):
            temp += num
            fmap[index] = temp
        
        #backward index mapped to reversed prefix sum 
        temp = 0
        for index, num in reversed(list(enumerate(nums))):
            temp += num
            bmap[index] = temp
        
        #get avg of 0 to curIndex, and curindex + 1 to end
        minimum = (math.inf, 0)
        for k, v in fmap.items():
            forward_diff = v//(k+1)
            backward_index = length - (k + 1)
            backward_diff = (bmap[k+1]) // backward_index if backward_index > 0 else 0 
            res = abs(forward_diff - backward_diff)
            if minimum[0] > res: minimum = (res, k)
        
        # print(minimum[1])
        return minimum[1]        

s = Solution()
nums = [2,5,3,9,5,3]
s.minimumAverageDifference(nums)
nums = [0]
s.minimumAverageDifference(nums)