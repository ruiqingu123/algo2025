from typing import List, Optional

from algo2025.二叉树.tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.helper1(self, nums, 0, len(nums) - 1)


    def helper1(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if (left > right):
            return None

        mid = (left + right) // 2
        root = TreeNode(nums[mid])

        root.left = self.helper1(nums, left, mid - 1)
        root.right = self.helper1(nums, mid + 1, right)

        return root