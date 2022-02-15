from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_counter = Counter(nums)

        for i in my_counter:
            if my_counter[i] == 1:
                return i


sol = Solution()

nums = [1,2,1,2,7]

print(sol.singleNumber(nums))