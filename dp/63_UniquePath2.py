from typing import List

class SolutionBF:
    """Brute force TLE"""
    def __init__(self):
        self.count = 0
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.helper(0, 0, obstacleGrid)
        return self.count

    def helper(self, x: int, y: int, grid: List[List[int]]):
        if(x == len(grid)): return
        if(y == len(grid[0])): return
        if(grid[x][y] == 1): return
        if(x == len(grid) - 1 and y == len(grid[0])-1): 
            self.count+=1
            return
        self.helper(x+1, y, grid)
        self.helper(x, y+1, grid)

class Solution:
    """
    Optimized with memoization
    Save # of paths to dest from a cell
    """

    from collections import defaultdict

    def __init__(self):
        self.memo = self.defaultdict(int)
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.helper(0, 0, obstacleGrid)

    def helper(self, x: int, y: int, grid: List[List[int]]):
        if (x,y) in self.memo: return self.memo[(x, y)]

        if(x == len(grid)): return 0
        if(y == len(grid[0])): return 0
        if(grid[x][y] == 1):
            self.memo[(x, y)] = 0 
            return 0
        if(x == len(grid) - 1 and y == len(grid[0])-1 and grid[x][y] != 1): return 1
        result1 = self.helper(x+1, y, grid)
        result2 = self.helper(x, y+1, grid)
        self.memo[(x, y)] = result1+result2
        return result1+result2

if __name__ == "__main__":
    c1 = [[0,0,0],[0,1,0],[0,0,0]]
    print(Solution().uniquePathsWithObstacles(c1))

    c2 = [[0,1],[0,0]]
    print(Solution().uniquePathsWithObstacles(c2))

    c3 = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]
    print(Solution().uniquePathsWithObstacles(c3))