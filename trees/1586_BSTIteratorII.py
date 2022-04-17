from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.values = []
        def traverse(node: TreeNode):
            if not node: return
            if node.left: traverse(node.left)
            if node: self.values.append(node.val)
            if node.right: traverse(node.right)
        traverse(root)
        self.start = -1 if self.values else None

    def hasNext(self) -> bool:
        return self.start is not None and self.start + 1 < len(self.values)

    def next(self) -> int:
        self.start += 1
        return self.values[self.start]

    def hasPrev(self) -> bool:
        return self.start is not None and self.start - 1 > -1

    def prev(self) -> int:
        self.start -= 1
        return self.values[self.start]