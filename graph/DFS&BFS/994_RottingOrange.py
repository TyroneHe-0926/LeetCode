from typing import List
from collections import defaultdict

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        graph = defaultdict(list)
        queue = []
        next_layer = []
        valid_oranges = 0
        visited = set()
        counter = 0

        if not any(1 in row for row in grid):
            return 0

        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                curnode = col_index + width*row_index
                if col == 1:
                    if (col_index-1<0 or row[col_index-1] == 0) and (col_index+1>width-1 or row[col_index+1] == 0) and (row_index-1<0 or grid[row_index-1][col_index] == 0) and (row_index+1>height-1 or grid[row_index+1][col_index] == 0):
                        return -1
                if col == 2 or col == 1:
                    valid_oranges += 1
                    if col == 2:
                        queue.append(curnode)
                    if col_index - 1 > -1:
                        if row[col_index-1] == 1 or row[col_index-1] == 2:
                            conn_node = curnode - 1
                            graph[curnode].append(conn_node)
                    if col_index + 1 < width:
                        if row[col_index+1] == 1 or row[col_index+1] == 2:
                            conn_node = curnode + 1
                            graph[curnode].append(conn_node)
                    if row_index - 1 > -1:
                        if grid[row_index-1][col_index] == 1 or grid[row_index-1][col_index] == 2:
                            conn_node = curnode - width
                            graph[curnode].append(conn_node)
                    if row_index + 1 < height: 
                        if grid[row_index+1][col_index] == 1 or grid[row_index+1][col_index] == 2:
                            conn_node = curnode + width
                            graph[curnode].append(conn_node)
        
        for node in queue:
            for child in graph[node]:
                if child not in queue:
                    next_layer.append(child)
        
        next_layer = list(dict.fromkeys(next_layer))

        while queue:
            node = queue.pop(0)
            
            if node in visited:
                continue
            
            visited.add(node)
        
            for child in graph[node]:
                if child not in visited:
                    queue.append(child)

            queue = list(dict.fromkeys(queue))

            if queue == next_layer:
                counter+=1
                next_layer = []

                for next_node in queue:
                    if next_node not in visited:
                        for child in graph[next_node]:
                            if child not in visited and child not in queue:
                                next_layer.append(child)

                next_layer = list(dict.fromkeys(next_layer))
        
        if len(visited) == valid_oranges:
            return counter-1

        return -1

if __name__ == "__main__":
    solution = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    grid3 = [[0],[0],[0],[2],[0],[0],[0],[1],[2]]

    print(solution.orangesRotting(grid))
    print(solution.orangesRotting(grid2))
    print(solution.orangesRotting(grid3))

"""
Tried UF, didnt know wtf happened
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        total_len = height * width

        if not any(1 in row for row in grid):
            return 0

        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if (col == 1 
                    and (col_index-1<0 or row[col_index-1] == 0)
                    and (col_index+1>width-1 or row[col_index+1] == 0)
                    and (row_index-1<0 or grid[row_index-1][col_index] == 0)
                    and (row_index+1>height-1 or grid[row_index+1][col_index] == 0)):
                    return -1

        counter = 0
        self.root = [i for i in range(total_len)]
        self.rank = [1] * total_len

        def is_one_head():
            heads = [self.find(node) for node in self.root]
            # print(heads)
            return all(head == heads[0] for head in heads)
            
        while not is_one_head():
            current_visit = []
            for row_index, row in enumerate(grid):
                for col_index, col in enumerate(row):
                    curnode = col_index + width*row_index
                    if col == 2 and curnode not in current_visit:
                        if col_index - 1 > -1:
                            if row[col_index-1] == 1:
                                conn_node = curnode - 1
                                current_visit.append(conn_node)
                                row[col_index-1] = 2
                                self.union(curnode, conn_node)
                            if row[col_index-1] == 0:
                                conn_node = curnode - 1
                                current_visit.append(conn_node)
                                self.union(curnode, conn_node)
                        if col_index + 1 < width:
                            if row[col_index+1] == 1:
                                conn_node = curnode + 1
                                current_visit.append(conn_node)
                                row[col_index+1] = 2
                                self.union(curnode, conn_node)
                            if row[col_index+1] == 0:
                                conn_node = curnode + 1
                                current_visit.append(conn_node)
                                self.union(curnode, conn_node)
                        if row_index - 1 > -1:
                            if grid[row_index-1][col_index] == 1:
                                conn_node = curnode - width
                                current_visit.append(conn_node)
                                grid[row_index-1][col_index] = 2
                                self.union(curnode, conn_node)
                            if grid[row_index-1][col_index] == 0:
                                conn_node = curnode - width
                                current_visit.append(conn_node)
                                self.union(curnode, conn_node)
                        if row_index + 1 < height: 
                            if grid[row_index+1][col_index] == 1:
                                conn_node = curnode + width
                                current_visit.append(conn_node)
                                grid[row_index+1][col_index] = 2
                                self.union(curnode, conn_node)
                            if grid[row_index+1][col_index] == 0:
                                conn_node = curnode + width
                                current_visit.append(conn_node)
                                grid[row_index+1][col_index] = 2
                                self.union(curnode, conn_node)
                            
            counter += 1

        return counter

    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root2 != root1:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root2] > self.rank[root1]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1
"""