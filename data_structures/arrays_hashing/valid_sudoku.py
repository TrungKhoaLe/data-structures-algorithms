from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                if num in rows[i] or num in columns[j] or num in boxes[(i // 3) * 3 + (j // 3)]:
                    return False
                
                rows[i].add(num)
                columns[j].add(num)
                boxes[(i // 3) * 3 + (j // 3)].add(num)
        return True


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]

    board1 = [[".",".",".",".","5",".",".","1","."],
              [".","4",".","3",".",".",".",".","."],
              [".",".",".",".",".","3",".",".","1"],
              ["8",".",".",".",".",".",".","2","."],
              [".",".","2",".","7",".",".",".","."],
              [".","1","5",".",".",".",".",".","."],
              [".",".",".",".",".","2",".",".","."],
              [".","2",".","9",".",".",".",".","."],
              [".",".","4",".",".",".",".",".","."]]
    board2 = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
    s = Solution()
    print(s.isValidSudoku(board2))
