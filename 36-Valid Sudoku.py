
"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""
"""
solution 1:
1. filter all row and column to only have number, because for a vaild sudoko, each row and col should have distinct num but many "."
2. vaild row, col and smallboard

"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        if self.validcolrow(board,n):
            return self.validsmallboard(board,n)
        else:
            return False

    def validcolrow(self, board,n):
        for c in range(n):
            row = [x for x in board[c] if x!="."]
            col = [board[r][c] for r in range(9) if board[r][c]!="."]

            if len(set(row))!=len(row) or len(set(col))!=len(col):
                return False
        return True

    def validsmallboard(self,board,n):
        for c in range(0,n,3):
            for r in range(0,n,3):
                smallboard = []
                for i in range(3):
                    for j in range(3):
                        num = board[r+i][c+j]
                        if num != ".":
                            smallboard.append(num)
                if len(set(smallboard))!=len(smallboard):
                    return False
        return True


"""
solution 2:
same idea like solution 1, but use hashset to speed up
"""
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):

                number = board[i][j]
                if number == ".": continue

                box = i//3 * 3 + j//3
                if number in rows[i]: return False
                if number in columns[j]: return False
                if number in boxes[box]: return False
                rows[i].add(number)
                columns[j].add(number)
                boxes[box].add(number)

        return True
