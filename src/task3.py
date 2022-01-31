class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_value = 0

        for item in accounts:
            if max_value == 0 or sum(item) > max_value:
                max_value = sum(item)
        return max_value


sol = Solution()
accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(sol.maximumWealth(accounts))
