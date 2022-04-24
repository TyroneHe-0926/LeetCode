from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            numleft, numright = nums[left], nums[right]
            
            # get the range of left and right half, at least one of them will be sorted
            rightrange, leftrange = range(nums[mid], numright+1), range(numleft, nums[mid]+1)
            if nums[mid] == target: return mid

            # 1. 
            # if target < mid and it is in the left range, we search the left half
            # if target > mid and it is in the right range, we search the right half
            if target < nums[mid] and target in leftrange: right = mid - 1
            elif target > nums[mid] and target in rightrange: left = mid + 1
            
            # 2. 
            # if target < mid and not in leftrange, and leftrange is sorted, it cant be in the left half anymore, so search right half
            # if target < mid and not in leftrange, but leftrange is unsorted, then we know right range is sorted, since mid is bigger than target, even though leftrange is unsorted, the only change to find it is left in the left half, so search left half
            elif target < nums[mid] and target not in leftrange and numleft < nums[mid]+1: left = mid + 1
            elif target > nums[mid] and target not in rightrange and nums[mid] < numright+1: right = mid - 1

            # 3.
            # if target > mid and not in rightrange, and rightrange is sorted, then it has to be in left range
            # if target > mid and not in rightrange, and rightrange is unsorted, then still search right half, as explained above
            elif target < nums[mid] and target not in leftrange and not numleft < nums[mid]+1: right = mid - 1
            elif target > nums[mid] and target not in rightrange and not nums[mid] < numright+1: left = mid + 1

        return -1

solution = Solution()
print(solution.search(nums = [4,5,6,7,0,1,2], target = 0))
print(solution.search(nums = [4,5,6,7,0,1,2], target = 3))
print(solution.search(nums = [1,2,4,5,6,7,0], target = 0))
print(solution.search(nums = [5,1,2,3,4], target = 1))
print(solution.search(nums = [4,5,6,7,8,1,2,3], target = 8))
print(solution.search(nums = [2,3,4,5,6,7,8,9,1], target=9))