from typing import Optional, List

from algo2025.二叉树.tree import TreeNode


class Solution:

    def __init__(self):
        self.result = []
        self.paths = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        self.binaryTreePaths1(root)
        return self.result


    def binaryTreePaths1(self, root: Optional[TreeNode]) -> List[str]:

        self.paths.append(str(root.val))

        if root.left is None and root.right is None:
            self.result.append("->".join(self.paths))
            return

        if root and root.left:
            self.binaryTreePaths(root.left)
            self.paths.pop()
        if root and root.right:
            self.binaryTreePaths(root.right)
            self.paths.pop()

        return self.result