

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res =[]

        def get_comb(start, temp, target):
            if target == 0:
                res.append(temp)

            for i in range(start, len(candidates)):
                print(temp)
                curr = candidates[i]
                temp_target = target - curr

                if temp_target >= 0:
                    get_comb(i, temp + [curr], temp_target)



        get_comb(0, [], target)

        return res

sol = Solution()

candidates = [1,2,6,7]
target = 7

print(sol.combinationSum(candidates, target))