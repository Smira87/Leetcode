from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        return (Counter(t) - Counter(s)).popitem()[0]

sol = Solution()

s = "abcde"
t = "abacde"


print(sol.findTheDifference(s, t))