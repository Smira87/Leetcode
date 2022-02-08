class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while num > 9:
            r = 0
            while num:
                r, num = r + num % 10, num // 10

            num = r


        return num


sol = Solution()

num = 38

print(sol.addDigits(num))

