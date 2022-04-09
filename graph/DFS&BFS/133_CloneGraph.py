from collections import defaultdict

class Node():
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
    
class Solution():
    
    def __init__(self):
        self.stack = []
        self.visited = set()
        self.clone_graph = defaultdict(Node)

    def cloneGraph(self, node: 'Node'):
        self.stack = [node]
        while self.stack:
            curnode = self.stack.pop()

            if curnode in self.visited:
                continue
            
            self.visited.add(curnode)
            tempnode = Node(curnode.val, curnode.neighbors)
            self.clone_graph[curnode.val] = tempnode
            for neighbors in curnode.neighbors:
                self.stack.append(neighbors)

"""
Leetcode solution
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):

    def __init__(self):
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}

    def cloneGraph(self, node):
        if not node:
            return node

        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]

        # Create a clone for the given node.
        # Note that we don't have cloned neighbors as of now, hence [].
        clone_node = Node(node.val, [])

        # The key is original node and value being the clone node.
        self.visited[node] = clone_node

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node
"""