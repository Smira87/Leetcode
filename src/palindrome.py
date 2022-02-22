class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        n = x

        while (n > 0):
            a = n % 10
            rev = rev * 10 + a
            n = n // 10

        return rev == x


sol = Solution()

x = 1221

print(sol.isPalindrome(x))