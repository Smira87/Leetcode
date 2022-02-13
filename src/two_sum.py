class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        my_map = {}

        for i in nums:
            if (target - i) in my_map:
                return [my_map[target - i], nums.index(i)]
            my_map[i] = nums.index(i)

sol = Solution()

nums =[2,7,11,15]
target = 9

print(sol.twoSum(nums, target))