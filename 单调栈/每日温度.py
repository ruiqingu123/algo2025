from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # 因为栈始终是单调递增的 
        stack = []
        res = [0] * len(temperatures)
        stack.append(0)
        for i in range(1,len(temperatures)):


            if(temperatures[i] <= temperatures[stack[-1]]):
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    idx = stack.pop()
                    res[idx] = i - idx
                stack.append(i)

        return res
