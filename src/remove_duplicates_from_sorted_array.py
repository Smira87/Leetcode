import collections

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ht = collections.defaultdict(int)
        k = 0
        while k < len(nums):
            ht[nums[k]] += 1
            if ht[nums[k]] > 2:
                nums.pop(k)
            else:
                k += 1

        print(nums)


sol = Solution()

nums = [0,0,1,1,1,1,2,3,3]

sol.removeDuplicates(nums)



