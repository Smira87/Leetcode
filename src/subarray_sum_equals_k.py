class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        current_sum = 0
        map = {0: 1}
        res = 0

        for i in nums:
            current_sum += i
            res += map.get(current_sum - k, 0)
            if current_sum in map:
                map[current_sum] += 1
            else:
                map[current_sum] = 1

        return res


sol = Solution()
nums = [1, 2, 3, 4]
k = 3

print(sol.subarraySum(nums, k))