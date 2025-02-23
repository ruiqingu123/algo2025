import collections
from typing import Optional, List

from algo2025.二叉树.tree import TreeNode


class Solution:



    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        list1 = []
        queue1 = collections.deque()
        queue1.append(root)


        while len(queue1)!=0:
            size = len(queue1)
            sum = 0

            for i in range(size):
                node = queue1.popleft()

                if node.left:
                    queue1.append(node.left)
                if node.right:
                    queue1.append(node.right)
                sum+=node.val

            list1.append(sum/size)

        return list1
