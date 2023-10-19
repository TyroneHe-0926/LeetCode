from typing import List

class SolutionBF:
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.memo = {}
        self.minsum = float('inf')

        self.helper(0, 0, 0, grid)
        return int(self.minsum)

    def helper(self, x, y, sum, grid: List[List[int]]):
        if x >= len(grid): return
        if y >= len(grid[0]): return

        sum += grid[x][y]

        if x == len(grid)-1 and y == len(grid[0])-1:
            self.minsum = min(sum, self.minsum)
            return sum
            
        self.helper(x, y+1, sum, grid)
        self.helper(x+1, y, sum, grid)

class SolutionMemo:
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.memo = {}

        return self.helper(0, 0, grid)

    def helper(self, x, y, grid: List[List[int]]):
        if x >= len(grid): return 
        if y >= len(grid[0]): return 

        if x == len(grid)-1 and y == len(grid[0])-1: return grid[x][y]

        rightsum, downsum = None, None

        if (x, y+1) in self.memo: 
            rightsum = self.memo[(x, y+1)]
        else: 
            rightsum = self.helper(x, y+1, grid)
            self.memo[(x, y+1)] = rightsum
        
        if (x+1, y) in self.memo:
            downsum = self.memo[(x+1, y)]
        else:
            downsum = self.helper(x+1, y, grid)
            self.memo[(x+1, y)] = downsum

        if rightsum is None: return grid[x][y] + downsum
        if downsum is None: return grid[x][y] + rightsum
        
        return grid[x][y] + min(downsum, rightsum)