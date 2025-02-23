# https://leetcode.cn/problems/spiral-matrix-ii/
from pprint import pprint
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        startX = 0
        startY = 0
        offset = 1
        count = 1

        # 左闭右开进行遍历
        res = [[0] * n for _ in range(n)]
        for _ in range(0, n // 2):

            x, y = startX, startY

            while y < n - offset:
                res[x][y] = count
                count += 1
                y += 1
            while x < n - offset:
                res[x][y] = count
                count += 1
                x += 1
            while y > startY:
                res[x][y] = count
                count += 1
                y -= 1
            while x > startX:
                res[x][y] = count
                count += 1
                x -= 1

            startX += 1
            startY += 1
            offset += 1


        if n % 2 == 1:
            res[n // 2][n // 2] = count

        return res


if __name__ == '__main__':
    print(6 // 2)
    res = Solution().generateMatrix(6)
    pprint(res)
