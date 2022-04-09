from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_paths = []
        target = len(graph) - 1

        if not graph:
            return []
        
        queue = [[0]]

        while queue:
            cur_path = queue.pop(0)
            node = cur_path[-1]

            if node == target:
                all_paths.append(cur_path)
                continue

            for connected in graph[node]:
                appended_path = cur_path.copy()
                appended_path.append(connected)
                queue.append(appended_path)

        return all_paths


if __name__ == "__main__":
    solution = Solution()
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(solution.allPathsSourceTarget(graph))

"""
DFS

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            path.append(node)
            if node == len(graph) - 1:
                paths.append(path.copy())
                return

            next_nodes = graph[node]
            
            for next_node in next_nodes:
                dfs(next_node)
                path.pop()

        paths = []
        path = []
        if not graph:
            return paths
        dfs(0)
        return paths

1: path=[0], next_nodes = 1,2, dfs(1)
2: path=[0,1], next_nodes = 3, dfs(3)
3: path = [0,1,3], returned, pop 3
4: path = [0,1], pop1
5: path = [0,2], next_nodes = 3, dfs(3)
6: path = [0,2,3], returned, pop3 
...
"""

"""
BFS

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_paths = []
        target = len(graph) - 1

        if not graph:
            return []
        
        queue = [[0]]

        while queue:
            cur_path = queue.pop(0)
            node = cur_path[-1]

            if node == target:
                all_paths.append(cur_path)
                continue

            for connected in graph[node]:
                appended_path = cur_path.copy()
                appended_path.append(connected)
                queue.append(appended_path)

        return all_paths
"""