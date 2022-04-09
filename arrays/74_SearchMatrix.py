from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            head, tail = row[0], row[-1]
            if target <= tail and target >= head:
                return self.bin_search(row, target)
        return False

    def bin_search(self, arr: List[int], target):
        left, right, mid = 0, len(arr)-1, 0
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target: return True
            elif arr[mid] > target: right = mid-1
            else: left = mid + 1
        return False

solution = Solution()
print(solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
print(solution.searchMatrix(matrix = [[2],[4], [6], [8],[9]], target = 8))