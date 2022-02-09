import collections

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        my_counter = collections.Counter(nums)
        res = 0
        for i in my_counter:
            if k == 0 and my_counter[i] > 1:
                res += 1
            elif k > 0 and i + k in my_counter:
                res += 1
        return res

sol = Solution()

nums = [3,1,4,1,5]

k = 0

print(sol.findPairs(nums, k))