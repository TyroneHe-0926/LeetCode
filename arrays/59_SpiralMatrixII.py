from typing import List

class Solution:
    #github copilot solution :o cra
    """ Pattern
    1  2  3  4
    12 13 14 5
    11 16 15 6
    10 9  8  7

    00 01 02 03 13 23 33 32 31 30 20 10 11 12 22 21

    1 2 3
    8 9 4
    7 6 5

    00 01 02 12 22 21 20 10 11
    """
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        row, col = 0, 0
        num = 1
        while num <= n * n:
            while col < n and matrix[row][col] == 0:
                matrix[row][col] = num
                col += 1
                num += 1
            col -= 1
            row += 1
            while row < n and matrix[row][col] == 0:
                matrix[row][col] = num
                row += 1
                num += 1
            row -= 1
            col -= 1
            while col >= 0 and matrix[row][col] == 0:
                matrix[row][col] = num
                col -= 1
                num += 1
            col += 1
            row -= 1
            while row >= 0 and matrix[row][col] == 0:
                matrix[row][col] = num
                row -= 1
                num += 1
            row += 1
            col += 1
        return matrix

class Solution:
    """
    Start with the empty matrix, add the numbers in reverse order until we added the number 1.
    Always rotate the matrix clockwise and add a top row:
    """
    def generateMatrix(self, n):
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [list(range(lo, hi))] + list(zip(*A[::-1]))
        return A

class Solution:
    """
    Initialize the matrix with zeros, 
    then walk the spiral path and write the numbers 1 to n*n. 
    Make a right turn when the cell ahead is already non-zero."""
    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A