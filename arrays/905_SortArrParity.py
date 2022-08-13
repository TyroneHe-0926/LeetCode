from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        left, right = 0, len(nums)-1
        for num in nums:
            if not num % 2: 
                result[left] = num
                left += 1
            else:
                result[right] = num
                right -= 1
        return result