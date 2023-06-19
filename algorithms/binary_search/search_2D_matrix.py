from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n_rows, n_cols = len(matrix), len(matrix[0])
        top, bot = 0, n_rows - 1
        
        # binary search row-wise
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        if not top <= bot:
            return False

        # binary search on the found row
        row = (top + bot) // 2
        l, r = 0, n_cols - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m - 1
            else:
                return True
        return False



if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    s = Solution()
    print(s.searchMatrix(matrix, target))
