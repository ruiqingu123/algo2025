import collections
from typing import Optional, List

from algo2025.二叉树.tree import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)

        res = []
        while len(queue) > 0:
            size = len(queue)
            tmp = []

            for i in range(size):
                node = queue.popleft()

                if node:
                    tmp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            res.append(tmp.copy())

        for idx, val in enumerate(res):
            if idx % 2 == 1:
                res[idx] = val[::-1]
        return res

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    res = Solution().zigzagLevelOrder(root)
    print(res)