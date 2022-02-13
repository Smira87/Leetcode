from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums) + 1):
            res += (list(combinations(nums, i)))

        return  res

sol = Solution()

nums = [1,2,3]

print(sol.subsets(nums))