from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        my_counter = Counter(nums)

        return max(my_counter,  key = my_counter.get)

sol = Solution()

nums = [2,2,1,1,1,2,2]

print(sol.majorityElement(nums))