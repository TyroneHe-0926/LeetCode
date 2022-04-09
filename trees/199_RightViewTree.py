from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view, queue = [], deque([root])
        if not root: return view
        while queue:
            view.append(queue[-1].val)
            next_layer = deque([])
            for node in queue:
                if node.left: next_layer.append(node.left)
                if node.right: next_layer.append(node.right)
            queue = next_layer
        
        return view


solution = Solution()
tree1 = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4)), right=TreeNode(val=3))
print(solution.rightSideView(tree1))
# print(solution.rightSideView(TreeNode(val=10)))
tree1 = TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=5)), right=TreeNode(val=3, right=TreeNode(val=4, left=TreeNode(val=18, left=TreeNode(val=19, right=TreeNode(val=20)))))) # 1 3 4 18 19 20
print(solution.rightSideView(tree1))