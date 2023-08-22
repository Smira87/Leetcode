import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        for i in s:
            if i.isalnum():
                n += i.lower()
        if n == n[::-1]:
            return True
        return False

s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))
