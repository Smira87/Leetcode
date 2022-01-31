class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max(sum(i) for i in accounts)



sol = Solution()
accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(sol.maximumWealth(accounts))
