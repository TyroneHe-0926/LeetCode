from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    My way of deleting the keynode,
    then insert all the keynodes child back to the new root where the keynode is deleted
    But this is pretty much O(h), one for search one for insert (or both O(log n) actually)
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        self.keynode, inserts = None, []
        def search(root: TreeNode, key):
            if root and root.left:
                if root.left.val == key:
                    self.keynode = root.left
                    root.left = None
                    return
                else: search(root.left, key)
            if root and root.right:
                if root.right.val == key:
                    self.keynode = root.right
                    root.right = None
                    return 
                else: search(root.right, key)
        
        def traverse(root: TreeNode):
            if root and root.left: traverse(root.left)
            inserts.append(root.val)
            if root and root.right: traverse(root.right)
        
        if root and root.val == key:
            self.keynode = root
            root = None
        
        search(root, key)
        if self.keynode and self.keynode.right: traverse(self.keynode.right)
        if self.keynode and self.keynode.left: traverse(self.keynode.left)
        
        if inserts and not root:
            root = TreeNode(inserts[0])
            inserts = inserts[1:]
        
        while inserts:
            val = inserts.pop()
            self.bst_insert(root, val)
        
        return root

    def bst_insert(self, root: TreeNode, nval):
        if nval < root.val:
            if root.left: self.bst_insert(root.left, nval)
            else: root.left = TreeNode(nval)
        elif nval > root.val:
            if root.right: self.bst_insert(root.right, nval)
            else: root.right = TreeNode(nval)


class Solution:
    """LC solution using predecssor and successor"""
    def successor(self, root):
        """
        Smallest node thats bigger than the root in the root's right subtree
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        """
        Biggest node thats smaller than the root in the root's left subtree
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root