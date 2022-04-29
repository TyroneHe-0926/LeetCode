from typing import List
from collections import defaultdict

class Solution:
    """BF TLE Obvisouly .. """
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        h, w, path, paths = len(heights), len(heights[0]), [], []
        graph, dest = defaultdict(list), (h-1, w-1)
        hrange, wrange = range(0, h), range(0, w)
        for row in range(h):
            for col in range(w):
                if col - 1 in wrange: graph[(row, col, heights[row][col])].append((row, col-1, heights[row][col-1]))
                if col + 1 in wrange: graph[(row, col, heights[row][col])].append((row, col+1, heights[row][col+1]))
                if row - 1 in hrange: graph[(row, col, heights[row][col])].append((row-1, col, heights[row-1][col]))
                if row + 1 in hrange: graph[(row, col, heights[row][col])].append((row+1, col, heights[row+1][col]))
        
        def dfs(x, y, height, seen):
            path.append((x,y,height))
            seen.append((x, y))
            if (x, y) == dest:
                paths.append(path.copy())
                return
            for (nx, ny, nh) in graph[(x, y, height)]:
                if (nx, ny) not in seen:
                    dfs(nx, ny, nh, seen)
                    path.pop()
                    seen.pop()

        dfs(0, 0, heights[0][0], [])
        #and then find min from all paths
    
class Solution:
    """Union Find O(mn log(mn))"""
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        h, w = len(heights), len(heights[0])
        self.root, self.rank = [i for i in range(h*w)], [1] * (h*w)

        #store all edges between 2 nodes, and the sort by their different ascending
        edge_list = []
        for current_row in range(h):
            for current_col in range(w):
                if current_row > 0:
                    difference = abs(
                        heights[current_row][current_col] -
                        heights[current_row - 1][current_col])
                    edge_list.append(
                        (difference, current_row * w + current_col,
                         (current_row - 1) * w + current_col))
                if current_col > 0:
                    difference = abs(
                        heights[current_row][current_col] -
                        heights[current_row][current_col - 1])
                    edge_list.append(
                        (difference, current_row * w + current_col, current_row
                         * w + current_col - 1))
        edge_list.sort()

        """
        After every union, check if the source cell (0) and destination cell (row * col - 1) are connected. If yes, the absolute difference between the current edge is our result. Since we access the edges in increasing order of difference, and the current edge connected the source and destination cell, we are sure that the current difference is the maximum absolute difference in our path with minimum efforts.
        """

        for difference, x, y in edge_list:
            self.union(x, y)
            if self.find(0) == self.find(h*w-1):
                return difference
        return 0
    
    def find(self, node):
        if self.root[node] == node: return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.rank[root2] > self.rank[root2]: self.root[root1] = root2
            else: self.root[root2] = root1

"""Binary Search with dfs/bfs ????"""
class Solution:
    """BFS"""
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        def canReachDestinaton(mid):
            visited = [[False]*col for _ in range(row)]
            queue = [(0, 0)]  # x, y
            while queue:
                x, y = queue.pop(0)
                if x == row-1 and y == col-1:
                    return True
                visited[x][y] = True
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    adjacent_x = x + dx
                    adjacent_y = y + dy
                    if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[adjacent_x][adjacent_y]:
                        current_difference = abs(
                            heights[adjacent_x][adjacent_y]-heights[x][y])
                        if current_difference <= mid:
                            visited[adjacent_x][adjacent_y] = True
                            queue.append((adjacent_x, adjacent_y))

        left = 0
        right = 10000000
        while left < right:
            mid = (left + right)//2
            if canReachDestinaton(mid):
                right = mid
            else:
                left = mid + 1
        return left

class Solution:
    """DFS"""
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        def canReachDestinaton(x, y, mid):
            if x == row-1 and y == col-1:
                return True
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                adjacent_x = x + dx
                adjacent_y = y + dy
                if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[
                        adjacent_x][adjacent_y]:
                    current_difference = abs(
                        heights[adjacent_x][adjacent_y]-heights[x][y])
                    if current_difference <= mid:
                        visited[adjacent_x][adjacent_y] = True
                        if canReachDestinaton(adjacent_x, adjacent_y, mid):
                            return True
        left = 0
        right = 10000000
        while left < right:
            mid = (left + right)//2
            visited = [[False]*col for _ in range(row)]
            if canReachDestinaton(0, 0, mid):
                right = mid
            else:
                left = mid + 1
        return left

solution = Solution()
print(solution.minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]]))
print(solution.minimumEffortPath(heights = [[1,2,3],[3,8,4],[5,3,5]]))
print(solution.minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))