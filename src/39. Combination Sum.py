from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if i >= len(candidates) or total > target:
                return
            if total == target:
                res.append(cur.copy())
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


candidates = [2, 3, 6, 7]
target = 7

sol = Solution()
print(sol.combinationSum(candidates, target))