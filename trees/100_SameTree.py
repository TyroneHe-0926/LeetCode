from turtle import right
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def pre_order_traverse(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if not node1 and not node2:
                return True
            if node1 is None and node2 is not None:
                return False
            if node2 is None and node1 is not None:
                return False
            if node1.val != node2.val:
                return False
            comp_left = pre_order_traverse(node1.left, node2.left)
            comp_right = pre_order_traverse(node1.right, node2.right)
            return comp_left and comp_right
                
        return pre_order_traverse(p, q)

solution = Solution()
root1node = TreeNode(val=2, left=None, right=None)
root1 = TreeNode(val=1, left=root1node, right=None)
root2node = TreeNode(val=1, left=None, right=None)
root2 = TreeNode(val=2, left=None, right=root2node)
print(solution.isSameTree(root1,root2))