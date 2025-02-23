from typing import List


class Solution:



    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:


        stack = []
        dic1 = {}
        stack.append(nums2[0])
        for i in range(1,len(nums2)):
            if nums2[i] <= stack[-1]:
                stack.append(nums2[i])
            else:
                while stack and nums2[i] > stack[-1]:
                    dic1[stack.pop()] = nums2[i]
                stack.append(nums2[i])

        res = []

        for i in range(len(nums1)):
            res.append(dic1.get(nums1[i],-1))

        return res