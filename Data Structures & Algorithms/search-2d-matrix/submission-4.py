class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRows = len(matrix)
        nCols = len(matrix[0])
        l = 0
        r = len(matrix) * (len(matrix[0])) -1
        mid = (l+r) // 2

        while l <= r:
            row = mid //nCols
            col = mid % nCols
            if matrix[row][col] < target:
                l = mid + 1
                mid = (l+r) // 2
            elif matrix[row][col] > target:
                r = mid -1
                mid = (l+r) // 2
            else:
                return True
        
        return False

