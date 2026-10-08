class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        bestRow = top
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] > target:
                bottom = row - 1
            else:
                bestRow = row
                top = row + 1
        left = 0
        right = len(matrix[bestRow]) - 1
        while left <= right:
            cell = (left + right) // 2
            if matrix[bestRow][cell] < target:
                left = cell + 1
            elif matrix[bestRow][cell] > target:
                right = cell - 1
            else:
                return True
        return False