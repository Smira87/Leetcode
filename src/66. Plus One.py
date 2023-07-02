class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = ""
        for number in digits:
            strings += str(number)
        temp = int(strings) + 1
        res = []
        for i in str(temp):
            res.append(int(i))
        return res