class Solution(object):
    def findAnagrams(self, s, p):
        scount = [0] * 26
        pcount = [0] * 26
        x = []
        for i in p:
            pcount[ord(i) - ord('a')] += 1
        for j in range(len(s)):
            scount[ord(s[j]) - ord('a')] += 1
            if j >= len(p):
                scount[ord(s[j - len(p)]) - ord('a')] -= 1
            if scount == pcount:
                x.append(j - len(p) + 1)
        return x

sol = Solution()
s = "cbabbabacd"
p = "abc"



print(sol.findAnagrams(s, p))

