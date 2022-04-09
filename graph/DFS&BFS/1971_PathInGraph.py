from typing import List
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        queue = [start]
        visited = set()

        while queue:
            curnode = queue.pop(0)
            
            if curnode == end:
                return True

            if curnode in visited:
                continue

            visited.add(curnode)

            for node in graph[curnode]:
                queue.append(node)
        
        return False


if __name__ == "__main__":
    solution = Solution()
    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination = 5
    print(solution.validPath(n, edges, source, destination))

"""
DFS
from typing import List
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        adjacency_list = defaultdict(list)
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
        
        stack = [start]
        visited = set()
        
        while stack:
            # Get the current node.
            node = stack.pop()
            
            # Check if we have reached the target node.
            if node == end:
                return True
            
            # Check if we've already visited this node.
            if node in visited:
                continue
            visited.add(node)
            
            # Add all neighbors to the stack.
            for neighbor in adjacency_list[node]:
                stack.append(neighbor)
        
        # Our stack is empty and we did not reach the end node.
        return False
"""

"""
My UF way
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.root = [i for i in range(n)]
        self.rank = [1] * n

        for (node1, node2) in edges:
            self.union(node1, node2)

        head1 = self.find(source)
        head2 = self.find(destination)

        return head1 == head2

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root2] > self.rank[root1]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1

    def find(self, node):
        while self.root[node] != node:
            node = self.root[node]
        
        return node
"""