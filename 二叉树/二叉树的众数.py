from typing import Optional, List

from algo2025.二叉树.tree import TreeNode


class Solution:

    def __init__(self):
        self.dict = {}

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.helper(root)
        max_count = max(self.dict.values())
        return [key for key, value in self.dict.items() if value == max_count]


    def helper(self,root: Optional[TreeNode]):
        if root is None:
            return
        self.dict[root.val] = self.dict.get(root.val, 0) + 1
        self.helper(root.left)
        self.helper(root.right)