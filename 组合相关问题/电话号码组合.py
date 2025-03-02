from typing import List


class Solution:

    def __init__(self):
        self.dict = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
            "1":"",
        }

        self.res = []
        self.path = ""

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.helper(digits,0)
        return self.res

    def helper(self,digits: str,index:int):

        if index == len(digits):
            self.res.append(self.path)
            return

        digit = digits[index]

        for char in self.dict[digit]:
            self.path += char
            self.helper(digits,index+1)
            self.path = self.path[:-1]