class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)

        if len(str(y)) <= 1:
            return True
        if y[-1:] == y[:1]:
            return self.isPalindrome(y[1:-1])

        return False


sol = Solution()

x = 1221

print(sol.isPalindrome(x))