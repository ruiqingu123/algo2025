from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        temperatures = nums + nums
        # 因为栈始终是单调递增的
        stack = []
        res = [-1] * len(temperatures)
        stack.append(0)
        for i in range(1, len(temperatures)):

            if (temperatures[i] <= temperatures[stack[-1]]):
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    idx = stack.pop()
                    res[idx] = temperatures[i]
                stack.append(i)

        return res[:len(nums)]
if __name__ == '__main__':
    a = [5,4,3,2,1]
    res = Solution().nextGreaterElements(a)
    print(res)