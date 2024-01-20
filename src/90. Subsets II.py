from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

            # All subsets that do not include nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res



sol = Solution()
nums = nums = [1,2,2]
print(sol.subsetsWithDup(nums))