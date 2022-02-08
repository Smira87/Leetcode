class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) > 1:
            num = sum(int(i) for i in str(num))

        return num

sol = Solution()

num = 38

print(sol.addDigits(num))

