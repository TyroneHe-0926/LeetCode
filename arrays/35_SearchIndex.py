from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right, mid = 0, len(nums)-1, 0
        while left <= right:
            mid = (right+left)//2
            if nums[mid] == target: return mid
            elif nums[mid] < target: left = mid+1
            else: right = mid-1 
    
        if nums[mid] < target: return mid+1
        else: return mid

class SolutionLC:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left

solution = Solution()
print(solution.searchInsert(nums = [1,3,5,6], target = 0))
print(solution.searchInsert(nums = [1,3,5,6], target = 2))
print(solution.searchInsert(nums = [1,3,5,6], target = 7))
print(solution.searchInsert(nums = [1,3], target = 2))