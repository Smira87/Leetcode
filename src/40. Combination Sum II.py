from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target < 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()

                prev = candidates[i]

        backtrack([],0, target)
        return res


sol = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(sol.combinationSum2(candidates,target))