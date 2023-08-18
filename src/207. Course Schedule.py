from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        preMap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True

            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

sol = Solution()
print(sol.canFinish(7, [[1, 2],[3, 4],[1, 3]]))
