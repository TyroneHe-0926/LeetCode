from typing import List
from copy import deepcopy

class Solution:
    """Solution with O(1) space, tho i think my shit is beating 80% ?"""
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                print(f"Switching {matrix[j][i]} with {matrix[i][j]}")
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

"""
My shit
def rotate(self, matrix: List[List[int]]) -> None:
    temp_matrix = deepcopy(matrix)
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            matrix[row_index][col_index] = temp_matrix[col_index][row_index]
        matrix[row_index] = matrix[row_index][::-1]

"""

solution = Solution()
m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
(solution.rotate(m1))
# (solution.rotate(m2))