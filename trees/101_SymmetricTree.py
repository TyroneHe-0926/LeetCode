from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def pre_tra_comp(leftnode: Optional[TreeNode], rightnode: Optional[TreeNode]):
            if not leftnode and not rightnode:
                return True
            if ((not leftnode and rightnode) or (not rightnode and leftnode)):
                return False
            if leftnode.val != rightnode.val:
                return False
            if pre_tra_comp(leftnode.left, rightnode.right) and pre_tra_comp(leftnode.right, rightnode.left):
                return True
            else:
                return False
        
        if not root.left and root.right:
            return False
        elif not root.right and root.left:
            return False
        elif not root.left and not root.right:
            return True
        else:
            return pre_tra_comp(root.left, root.right)

solution = Solution()
node6 = TreeNode(val=1, left=TreeNode(val=2))
node7 = TreeNode(val=3)
node5 = TreeNode(val=4)
node4 = TreeNode(val=3)
node3 = TreeNode(val=2, left=node6, right=node7)
node2 = TreeNode(val=2, left=node4, right=node5)
root = TreeNode(val=1, left=node2, right=node3)
print(solution.isSymmetric(root))