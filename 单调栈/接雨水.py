from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        res = 0
        stack.append(0)
        for i in range(1,len(height)):
            if height[i] <= height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:
                    midIdx = stack.pop()
                    if stack:
                        rightIdx = i
                        leftIdx = stack[-1]
                        height1 = min(height[leftIdx],height[rightIdx]) - height[midIdx]
                        width = rightIdx - leftIdx - 1
                        res += height1 * width

                stack.append(i)
        return res
if __name__ == '__main__':
    input1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = Solution().trap(input1)
    print(res)