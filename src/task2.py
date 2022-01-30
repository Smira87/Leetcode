class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < k:
            for i in range(k):
                last_element = nums.pop()
                nums.insert(0, last_element)
        else:
            aux_array1 = nums[-k:]
            aux_array2 = nums[:-k]

            nums[:] = aux_array1 + aux_array2



sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
sol.rotate(nums, 3)
#sol.rotate_one_by_one()
print(nums)

