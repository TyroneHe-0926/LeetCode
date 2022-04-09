from typing import List
from copy import deepcopy

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        for i in range(3):
            rotated_matrix = self.rotate(mat)
            if rotated_matrix == target:
                return True
        return False
    
    def rotate(self, matrix: List[List[int]]):
        temp_matrix = deepcopy(matrix)
        for row_index, row in enumerate(matrix):
            for col_index, col in enumerate(row):
                matrix[row_index][col_index] = temp_matrix[col_index][row_index]
            matrix[row_index] = matrix[row_index][::-1]
        return matrix
    
solution = Solution()
mat, target = [[0,1],[1,0]], [[1,0],[0,1]]
print(solution.findRotation(mat, target))
mat, target = [[0,1],[1,1]], [[1,0],[0,1]]
print(solution.findRotation(mat, target))
mat, target = [[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]
print(solution.findRotation(mat, target))