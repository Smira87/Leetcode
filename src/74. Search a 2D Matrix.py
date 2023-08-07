from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n -1

        while left <= right:
            mid = (left + right) // 2
            mid_row, mid_col = divmod(mid, n)
            if target == matrix[mid_row][mid_col]:
                return True
            elif target < matrix[mid_row][mid_col]:
                right = mid - 1
            else:
                left = mid + 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 12

sol = Solution()
print(sol.searchMatrix(matrix, target))