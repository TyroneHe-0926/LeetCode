from typing import List
from collections import defaultdict

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for (src, dst) in edges:
            graph[src].append(dst)
        
        stack = [source]
        visited = set()

        if len(graph[destination]) != 0:
            return False

        while stack:
            node = stack.pop()
            if node in graph[node]:
                return False
            
            for connected in graph[node]:
                if node in graph[connected]:
                    return False
                
            if node == destination or node in visited:
                continue

            visited.add(node)

            if not graph[node]:
                return False
            
            for connected in graph[node]:
                stack.append(connected)
        
        return True

if __name__ == "__main__":
    solution = Solution()
    n = 4
    edges = [[0,1],[0,3],[1,2],[2,1]]
    source = 0
    destination = 3
    print(solution.leadsToDestination(n, edges, source, destination))

"""
DFS
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for (src, dst) in edges:
            graph[src].append(dst)
        
        stack = [source]
        visited = set()

        if len(graph[destination]) != 0:
            return False

        while stack:
            node = stack.pop()
            if node in graph[node]:
                return False
            
            for connected in graph[node]:
                if node in graph[connected]:
                    return False
                
            if node == destination or node in visited:
                continue

            visited.add(node)

            if not graph[node]:
                return False
            
            for connected in graph[node]:
                stack.append(connected)
        
        return True
"""