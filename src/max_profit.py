class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum, profit = float('inf'), 0

        for i in range(len(prices)):
            minimum = min(prices[i], minimum)
            profit = max(profit, prices[i] - minimum)

        return profit

sol = Solution()
prices = [7,1,5,3,6,4]

print(sol.maxProfit(prices))