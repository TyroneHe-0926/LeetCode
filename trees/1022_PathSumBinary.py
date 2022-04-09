from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionDFSRecur:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        path, values = [], []
        def dfs(node: Optional[TreeNode]):
            path.append(str(node.val))
            if not node.left and not node.right:
                values.append(int("".join(path), 2))
                return
            if node.left:
                dfs(node.left)
                path.pop()
            if node.right:
                dfs(node.right)
                path.pop()
        dfs(root)
        return sum(values)

class SolutionDFSIter:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack, values = [[root]], []
        while stack:
            path = stack.pop()
            node = path[-1]
            if not node.left and not node.right:
                values.append(int("".join([str(n.val) for n in path]),2))
            if node.right:
                new_path = path.copy()
                new_path.append(node.right)
                stack.append(new_path)
            if node.left:
                new_path = path.copy()
                new_path.append(node.left)
                stack.append(new_path)
        return sum(values)