
from typing import Optional, List
from algo2025.二叉树.tree import TreeNode
from queue import Queue


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        queue1 = Queue()
        queue1.put(root)
        resList = []
        while not queue1.empty():
            tmpList = []

            for _ in range(queue1.qsize()):
                tmpNode = queue1.get()
            tmpList.append(tmpNode.val)

            if tmpNode.left:
                queue1.put(tmpNode.left)
            if tmpNode.right:
                queue1.put(tmpNode.right)
            resList.append(tmpList)
        return resList


