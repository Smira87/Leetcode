import collections

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        ht = collections.defaultdict(int)

        for n1 in nums1:
            for n2 in nums2:
                ht[n1 + n2] += 1

        ans = 0
        for n3 in nums3:
            for n4 in nums4:
                ans += ht[-n3 - n4]

        return ans

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
sol = Solution()
print(sol.fourSumCount(nums1, nums2, nums3, nums4))