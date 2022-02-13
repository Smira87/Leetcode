class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        my_map = {}

        for i in range(len(nums)):
            if (target - nums[i]) in my_map:
                return [my_map[target - nums[i]], i]
            my_map[nums[i]] = i


sol = Solution()

nums = [3, 3]
target = 6

print(sol.twoSum(nums, target))