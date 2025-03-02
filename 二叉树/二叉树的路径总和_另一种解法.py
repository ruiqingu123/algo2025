from typing import Optional, List

from algo2025.二叉树.tree import TreeNode


def __init__(self):
    self.dic = {}
    self.paths = []


def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    self.binaryTreePaths1(root)
    return targetSum in self.dic


def binaryTreePaths1(self, root: Optional[TreeNode]) -> List[str]:
    self.paths.append(root.val)

    if root.left is None and root.right is None:
        self.dic[sum(self.paths)] = True
        return

    if root and root.left:
        self.binaryTreePaths1(root.left)
        self.paths.pop()
    if root and root.right:
        self.binaryTreePaths1(root.right)
        self.paths.pop()

    # return self.result