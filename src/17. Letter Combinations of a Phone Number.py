from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {"2": "abc",
               "3": "def",
               "4": "ghi",
               "5": "jkl",
               "6": "mno",
               "7": "pqrs",
               "8": "tuv",
               "9": "wxyz"}
        res = []
        def dfs(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for letter in map[digits[i]]:
                dfs(i + 1, cur + letter)
        if digits:
            dfs(0, "")
        return res

sol = Solution()
digits = "23"
print(sol.letterCombinations(digits))