from typing import List

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic1 = {}
        for i in nums:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1

        min_heap = []


        for k1,v in dic1.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap,(v,k1))
            else:
                tmp = min_heap[0]
                if v > tmp[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,(v,k1))


        res = []
        for i in min_heap:
            res.append(i[1])
        return res

if __name__ == '__main__':
    res = Solution().topKFrequent([4,1,-1,2,-1,2,3],2)
    print(res)