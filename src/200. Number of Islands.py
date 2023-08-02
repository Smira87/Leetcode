import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                raw, col = q.popleft()
                directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
                for dr, dc in directions:
                    if ((raw + dr) in range(rows) and
                        (col + dc) in range(cols) and
                        grid[raw + dr][col + dc] == "1" and
                        (raw + dr,col + dc) not in visit):
                        q.append((raw + dr, col + dc))
                        visit.add((raw + dr, col + dc))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands
