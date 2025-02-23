from typing import List


class Solution:

    def __init__(self):
        self.res = []
        self.tmp = []
        self.dic1 = {}

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        self.threeSum1(nums,0)
        return self.res


    def threeSum1(self,nums:List[int],startIdx:int):
        if len(self.tmp) == 3:
            if sum(self.tmp) == 0:
                paths = self.tmp.copy()
                paths = sorted(paths)

                if not self.dic1.get(str(paths)):
                    self.dic1[str(paths)] = 1
                    self.res.append(paths)
            return

        for i in range(startIdx,len(nums)):
            self.tmp.append(nums[i])
            self.threeSum1(nums,i+1)
            self.tmp.pop()


if __name__ == '__main__':
    a = [2,3,45,1]
    a = sorted(a)
    a
    print(a)
