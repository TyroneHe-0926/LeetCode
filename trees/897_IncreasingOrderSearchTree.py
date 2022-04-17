class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values = []
        def traverse(node: TreeNode):
            if node.left: traverse(node.left)
            if node: values.append(node.val)
            if node.right: traverse(node.right)
        traverse(root)
        new_root = None if not values else TreeNode(val=values[0])
        temp_node = new_root
        for val in values[1:]:
            temp_node.right = TreeNode(val=val)
            temp_node = temp_node.right
        return new_root

class Solution:
    """Recursion with relinking"""
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right