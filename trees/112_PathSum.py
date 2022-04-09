# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""DFS"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        path = []
        def dfs(node: Optional[TreeNode]):
            path.append(node)
            if not node.left and not node.right:
                result = 0
                for n in path:
                    result += n.val
                if result == targetSum: return True
            if node.left:
                if dfs(node.left): return True
                path.pop()
            if node.right:
                if dfs(node.right): return True
                path.pop()
            
        return dfs(root) or False

if __name__ == "__main__":
    node6 = TreeNode(val=-1, left=None, right=None)
    node4 = TreeNode(val=3, left=None, right=None)
    node3 = TreeNode(val=1, left=node6, right=None)
    node5 = TreeNode(val=-2, left=None, right=None)
    node2 = TreeNode(val=-3, left=node5, right=None)
    node1 = TreeNode(val=-2, left=node3, right=node4)
    root = TreeNode(val=1, left=node1, right=node2)
    solution = Solution()
    print(solution.hasPathSum(root, -1))

"""
BFS
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = deque([[root]])
        while queue:
            path = queue.popleft()
            if not path[-1].left and not path[-1].right:
                result = 0
                for n in path:
                    result += n.val
                if result == targetSum:
                    return True

            if path[-1].left:
                new_path = path.copy()
                new_path.append(path[-1].left)
                queue.append(new_path)
            if path[-1].right:
                new_path = path.copy()
                new_path.append(path[-1].right)
                queue.append(new_path)
        
        return False
"""