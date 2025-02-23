from typing import List


class Solution:
    def __init__(self):
        self.my_dic = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        self.my_dic1 = {}
        for k,v in self.my_dic.items():
            for item in v:
                self.my_dic1[item] = k
        self.res = []
        self.tmp = []


    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return [""]

        arr = []
        for i in range(len(digits)):
            arr+=(self.my_dic.get(digits[i]))

        # print(len(arr))
        # print("ARR===>",arr)
        self.letterCombinations1(arr,len(digits),0)
        return self.remove(self.res)

    # 同层的元素不插入
    def remove(self,combineList:List[str])->List[str]:
        res = []
        for list1 in combineList:
            tmpLevel = {}
            for i in list1:
                tmpLevel[self.my_dic1.get(i)] = i
            if len(tmpLevel) == len(list1):
                res.append("".join(list1))
        return res

    def letterCombinations1(self, combineListStr: List[str],k:int,start:int) -> List[str]:
        if len(self.tmp) == k:
            paths = self.tmp.copy()
            # print(paths)
            self.res.append(paths)
            return


        #arr = ["a","b","c","d","e","f"]
        for i in range(start,len(combineListStr)):
            self.tmp.append(combineListStr[i])
            start = start+1
            self.letterCombinations1(combineListStr,k,start)
            self.tmp.pop()


if __name__ == '__main__':

    res = Solution().letterCombinations("23")


    print(res)