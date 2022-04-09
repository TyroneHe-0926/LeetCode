from typing import List
from collections import defaultdict

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        length = len(grid)
        target = length * length - 1
        graph = defaultdict(list)

        #consturct the graph
        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if col == 1:
                    continue
                gnode = col_index + (length * row_index)
                #check →
                if col_index + 1 < length and row[col_index+1] == 0:
                    connected_node = gnode + 1
                    graph[gnode].append(connected_node)
                #check ←
                if col_index - 1 > -1 and row[col_index-1] == 0:
                    connected_node = gnode - 1
                    graph[gnode].append(connected_node)
                #check ↑
                if row_index - 1 > -1 and grid[row_index-1][col_index] == 0:
                    connected_node = gnode - length
                    graph[gnode].append(connected_node)
                #check ↓
                if row_index + 1 < length and grid[row_index+1][col_index] == 0:
                    connected_node = gnode + length
                    graph[gnode].append(connected_node)
                #check ⇗
                if row_index - 1 > -1 and col_index + 1 < length and grid[row_index-1][col_index+1] == 0:
                    connected_node = gnode - length + 1
                    graph[gnode].append(connected_node)
                #check ⇖
                if row_index - 1 > -1 and col_index -1 > -1 and grid[row_index-1][col_index-1] == 0:
                    connected_node = gnode - length - 1
                    graph[gnode].append(connected_node)
                #check ⇘
                if row_index + 1 < length and col_index + 1 < length and grid[row_index+1][col_index+1] == 0:
                    connected_node = gnode + length + 1
                    graph[gnode].append(connected_node)
                #check ⇙
                if row_index + 1 < length and col_index - 1 > -1 and grid[row_index+1][col_index-1] == 0:
                    connected_node = gnode + length -1
                    graph[gnode].append(connected_node) 

        queue = [[0]]
        visited = set()

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node in visited:
                continue

            if node == target:
                return len(path)
            
            visited.add(node)
            for connected in graph[node]:
                appended_path = path.copy()
                appended_path.append(connected)
                queue.append(appended_path)
        
        return -1

if __name__ == "__main__":
    solution = Solution()
    grid1 = [[0,1],[1,0]]
    grid2 = [[0,0,0],[1,1,0],[1,1,0]]
    grid3 = [[1,0,0],[1,1,0],[1,1,0]]

    print(solution.shortestPathBinaryMatrix(grid1))
    print(solution.shortestPathBinaryMatrix(grid2))
    print(solution.shortestPathBinaryMatrix(grid3))