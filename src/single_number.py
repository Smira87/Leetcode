class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res

sol = Solution()

nums = [3,1,2,1,2]

print(sol.singleNumber(nums))