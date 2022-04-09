from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        w, h = len(grid[0]), len(grid)
        self.root = [i for i in range(w*h)]
        self.rank = [1] * (w*h)
        heads = set()

        for row in range(h):
            for col in range(w):
                node = w*row + col
                if grid[row][col] == '1':
                    if col-1 > -1 and grid[row][col-1] == '1': self.union(node, node-1)
                    if col+1 < w and grid[row][col+1] == '1': self.union(node, node+1)
                    if row-1 > -1 and grid[row-1][col] == '1': self.union(node, node-w)
                    if row+1 < h and grid[row+1][col] == '1': self.union(node, node+w)
                else:
                    self.root[node] = -1
        
        for node in self.root:
            if node != -1: heads.add(self.find(node))
        return len(heads)

    def find(self, node):
        if self.root[node] == node:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = self.root[root1]
                self.rank[root1] += 1
            elif self.rank[root2] > self.rank[root1]:
                self.root[root1] = self.root[root2]
                self.rank[root2] += 1
            else:
                self.root[root2] = self.root[root1]
                self.rank[root1] += 1

solution = Solution()
print(solution.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(solution.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

"""
DFS with cpp, didnt want to rewrite it into python anymore
BFS basically the same idea, check how many nodes triggers a BFS/DFS after seeing one starter node
and traverse all connected nodes while setting visited to 0
class Solution {
private:
  void dfs(vector<vector<char>>& grid, int r, int c) {
    int nr = grid.size();
    int nc = grid[0].size();

    grid[r][c] = '0';
    if (r - 1 >= 0 && grid[r-1][c] == '1') dfs(grid, r - 1, c);
    if (r + 1 < nr && grid[r+1][c] == '1') dfs(grid, r + 1, c);
    if (c - 1 >= 0 && grid[r][c-1] == '1') dfs(grid, r, c - 1);
    if (c + 1 < nc && grid[r][c+1] == '1') dfs(grid, r, c + 1);
  }

public:
  int numIslands(vector<vector<char>>& grid) {
    int nr = grid.size();
    if (!nr) return 0;
    int nc = grid[0].size();

    int num_islands = 0;
    for (int r = 0; r < nr; ++r) {
      for (int c = 0; c < nc; ++c) {
        if (grid[r][c] == '1') {
          ++num_islands;
          dfs(grid, r, c);
        }
      }
    }

    return num_islands;
  }
};
"""