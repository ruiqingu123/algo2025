from typing import Optional

from algo2025.二叉树.tree import TreeNode


class Solution:
    def traversal(self, cur: TreeNode, count: int) -> bool:
        if cur and not cur.left and not cur.right:
            return count == 0

        if cur.left:  # 左
            if self.traversal(cur.left, count - cur.left.val):  # 递归，处理节点
                return True

        if cur.right:  # 右
            if self.traversal(cur.right, count - cur.right.val):  # 递归，处理节点
                return True

        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.traversal(root, targetSum - root.val)