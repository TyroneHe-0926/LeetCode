from typing import List
from collections import defaultdict

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        w,h = len(grid[0]), len(grid)
        self.root = [i for i in range(w*h)]
        self.rank = [1] * (w*h)
        islandmap, maxm = defaultdict(int), 0

        for rindex, row in enumerate(grid):
            for cindex, num in enumerate(row):
                node = rindex*w+cindex
                if num == 1:
                    if cindex + 1 < w and row[cindex+1] == 1: self.union(node, node+1)
                    if cindex - 1 > -1 and row[cindex-1] == 1: self.union(node, node-1)
                    if rindex + 1 < h and grid[rindex+1][cindex] == 1: self.union(node, node+w)
                    if rindex - 1 > -1 and grid[rindex-1][cindex] == 1: self.union(node, node-w)
                else: self.root[node] = -1
        
        for node in self.root:
            if node != -1:
                head = self.find(node)
                islandmap[head] += 1
                maxm = max(maxm, islandmap[head])
        
        return maxm


    def find(self, node):
        if self.root[node] == node: return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.rank[root2] > self.rank[root1]:
                self.root[root1] = self.root[root2]
                self.rank[root2] += 1
            else:
                self.root[root2] = self.root[root1]
                self.rank[root1] += 1

solution = Solution()
print(solution.maxAreaOfIsland(grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]))
print(solution.maxAreaOfIsland(grid = [[0,0,0,0,0,0,0,0]]))