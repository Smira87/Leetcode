class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1rep = [0] * 26
        s2rep = [0] * 26
        res = 0

        for i in s1:
            s1rep[ord(i) - ord("a")] += 1

        for j in range(len(s2)):
            s2rep[ord(s2[j]) - ord("a")] += 1
            if j >= len(s1):
                s2rep[ord(s2[j - len(s1)]) - ord("a")] -= 1
            if s2rep == s1rep:
                res += 1

        return res

sol = Solution()

s1 = "o"
s2 = "eidbaooo"

print(sol.checkInclusion(s1, s2))

