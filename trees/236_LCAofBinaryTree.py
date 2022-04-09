from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """BFS"""
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ppath, qpath = deque([[root]]), deque([[root]])
        def bfs_traverse(node: 'TreeNode', target, path: deque):
            while path:
                curpath  = path.popleft()
                node = curpath[-1]
                if node.val == target:
                    return curpath
                if node.left:
                    newpath = curpath.copy()
                    newpath.append(node.left)
                    path.append(newpath)
                if node.right:
                    newpath = curpath.copy()
                    newpath.append(node.right)
                    path.append(newpath)
        
        ppath = bfs_traverse(root, p.val, ppath)
        qpath = bfs_traverse(root, q.val, qpath)

        for i in range(len(ppath)-1, -1, -1):
            if i < len(qpath) and qpath[i].val == ppath[i].val: return qpath[i]

class Solution:
    """DFS"""
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = {"ppath": [],"qpath": []}
        def traverse(node: 'TreeNode', target, path):
            paths[path].append(node)
            if node.val == target:
                return 1
            if node.left:
                if traverse(node.left, target, path): return 1
                else: paths[path].pop()
            if node.right:
                if traverse(node.right, target, path): return 1
                else: paths[path].pop()
        traverse(root, p.val, 'ppath')
        traverse(root, q.val, 'qpath')

        for i in range(len(paths['ppath'])-1, -1, -1):
            if i < len(paths['qpath']) and paths['qpath'][i].val == paths['ppath'][i].val: return paths['qpath'][i]

class Solution:
    """LC recursive using my original idea to check if both sides of a node has found p and q"""
    def lowestCommonAncestor(self, root, p, q):
        self.ans = None
        
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans