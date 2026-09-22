class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            m = (top + bottom) // 2
            if matrix[m][0] > target:
                bottom = m - 1
            else:
                top = m + 1
        row = bottom
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False