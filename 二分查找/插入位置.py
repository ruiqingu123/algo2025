from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        mid = 0
        while(left<=right):
            mid = (left+right) /2
            if nums[mid] > target:
                right = mid -1
            if nums[mid] < target:
                left = left +1
            if (nums[mid]==target):
                return mid

        if nums[mid] < target:
            return mid+1
        elif nums[mid]>target:
            return mid

