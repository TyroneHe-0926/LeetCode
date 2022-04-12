from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        width, height = len(grid[0]), len(grid)
        for i in range(k):
            grid = self.shift(grid, width, height)
        return grid
    
    def shift(self, grid, width, height):
        shifted = [[0 for x in range(width)] for y in range(height)] 
        for row in range(height):
            for col in range(width):
                if row == height - 1 and col == width - 1:
                    shifted[0][0] = grid[row][col]
                elif col == width - 1:
                    shifted[row+1][0] = grid[row][col]
                else:
                    shifted[row][col+1] = grid[row][col]
        return shifted

solution = Solution()
print(solution.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
# print(solution.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
# print(solution.shiftGrid([[1],[2],[3],[4],[7],[6],[5]], 23))
# print(solution.shiftGrid([[1,2,3,4,5,6]], 1))