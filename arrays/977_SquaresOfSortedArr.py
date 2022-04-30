from typing import List

class Solution:
    """Just Sort O(nlogn)"""
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([nums[i]**2 for i in range(len(nums))])

class Solution:
    """O(N)"""
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result