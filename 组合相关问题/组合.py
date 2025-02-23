from typing import List


class Solution:

    def __init__(self):
        self.res = []
        self.tmp = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combine1(n,k,1)
        return self.res

    def combine1(self,n:int,k:int,start:int):

        # 当前tmp的长度等于k 那么进行结果的收集
        if len(self.tmp) == k:
            paths = self.tmp.copy()
            self.res.append(paths)
            return

        # 1 2 3 4

        for i in range(start,n+1):
            self.tmp.append(i)
            self.combine1(n,k,i+1)
            # pop 的意义在于把上次的结果删除
            # 比如 [1,2] POP 2
            # 变成 [1,3]
            self.tmp.pop()

if __name__ == '__main__':
    res = Solution().combine(4,2)
    print(res)