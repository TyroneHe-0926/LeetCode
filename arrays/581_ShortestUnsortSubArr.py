from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        right, left = 0, 0
        for index, num in enumerate(nums):
            if index + 1 < len(nums) and nums[index+1] < num:
                left = index
                break
        
        for i in range(len(nums)-1, -1, -1):
            if index - 1 > -1 and nums[i-1] > nums[i]:
                right = i
                break
        
        return 0 if right == 0 and left == 0 else right - left + 1