from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0
            visit.add((i, j))
            perimetr = dfs(i + 1, j)
            perimetr += dfs(i, j + 1)
            perimetr += dfs(i - 1, j)
            perimetr += dfs(i, j - 1)
            return perimetr

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)

sol = Solution()
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(sol.islandPerimeter(grid))