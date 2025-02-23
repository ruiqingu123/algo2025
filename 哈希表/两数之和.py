from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        dict1 = {}

        for idx, k in enumerate(nums):
            if target - k in dict1 :
                return [dict1[target - k],idx ]
            dict1[k] = idx
        return None

if __name__ == '__main__':
    print( Solution().twoSum([3,3], 6) )