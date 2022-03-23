#
#  Title:       Sudoku Solver
#
#  Link:        https://leetcode.com/problems/sudoku-solver/
#
#  Difficulty:  Hard
#
#  Task:        Write a program to solve a Sudoku puzzle by filling the empty cells.
#               A sudoku solution must satisfy all of the following rules:
#                   - Each of the digits 1-9 must occur exactly once in each row.
#                   - Each of the digits 1-9 must occur exactly once in each column.
#                   - Each of the digits 1-9 must occur exactly once in each of the 9
#                     3x3 sub-boxes of the grid.
#
#  Example:     Input:  board = [["5","3",".",".","7",".",".",".","."],
#                                ["6",".",".","1","9","5",".",".","."],
#                                [".","9","8",".",".",".",".","6","."],
#                                ["8",".",".",".","6",".",".",".","3"],
#                                ["4",".",".","8",".","3",".",".","1"],
#                                ["7",".",".",".","2",".",".",".","6"],
#                                [".","6",".",".",".",".","2","8","."],
#                                [".",".",".","4","1","9",".",".","5"],
#                                [".",".",".",".","8",".",".","7","9"]]
#
#               Output: board = [['5','3','4','6','7','8','9','1','2'],
#                                ['6','7','2','1','9','5','3','4','8'],
#                                ['1','9','8','3','4','2','5','6','7'],
#                                ['8','5','9','7','6','1','4','2','3'],
#                                ['4','2','6','8','5','3','7','9','1'],
#                                ['7','1','3','9','2','4','8','5','6'],
#                                ['9','6','1','5','3','7','2','8','4'],
#                                ['2','8','7','4','1','9','6','3','5'],
#                                ['3','4','5','2','8','6','1','7','9']]
#
#  Contraints:  * board.length == 9
#               * board[i].length == 9
#               * board[i][j] is a digit or '.'.
#               * It is guaranteed that the input board has only one solution.
#

# Version 1.0.0 - A better revision would reuse the "need" variable

class SudokuSolver(object):
    def solveSudoku(self, board):
        unsolved = True
        while unsolved:
            # List of Lists containing the values still needed by each cell
            need=[]

            # Go through each row and determine what values are needed for each cell that is "."
            for r in range(9):
                need.append([])
                q = ["1","2","3","4","5","6","7","8","9"]
                for c in range(9):
                    if board[r][c] in q:
                        q.remove(board[r][c])
                for c in range(9):
                    if board[r][c] == ".":
                        need[r].append(q.copy())
                    else:
                        need[r].append([])

            # Go through each column and determine what values are needed for each cell that is "."  
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for rr in range(9):
                            if board[rr][c] != "." and board[rr][c] in need[r][c]:
                                need[r][c].remove(board[rr][c])

            # Go through each grid and determine what values are needed
            grid=[ [],[],[],[],[],[],[],[],[] ]
            for r in range(9):
                for c in range(9):
                    if board[r][c] != ".":
                        g = (int(r/3)*3) + int(c/3)
                        grid[g].append(board[r][c])

            # Apply grid values to each cell in the grid with a value of "."
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        g = (int(r/3)*3) + int(c/3)
                        for v in grid[g]:
                            if v in need[r][c]:
                                need[r][c].remove(v)
                        if len(need[r][c]) == 1:
                            board[r][c] = need[r][c][0]
                            need[r][c] = []

            # Check if all the cells have a value now
            unsolved = False
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        unsolved = True

        return board

if __name__ == "__main__":

    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]

    z = SudokuSolver()
    b = z.solveSudoku(board)
    for r in range(9):
        print(b[r])
