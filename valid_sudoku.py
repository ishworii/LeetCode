'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

class Solution:
    def check_rows(self,board):
        for i in board:
            s = set()
            for j in i:
                if j != '.' :
                    if j in s:
                        return False
                    s.add(j)
        return True
    
    
    def check_columns(self,board):
        for i in range(len(board)):
            s  = set()
            for j in range(len(board[i])):
                if board[j][i] != '.':
                    if board[j][i] in s:
                        return False
                    s.add(board[j][i])
        return True
    
    def check_sub_boxes(self,board):
        for i in range(0,9,3):
            for j in range(0,9,3):
                s = set()
                for x in range(i,i+3):
                    for y in range(j,j + 3):
                        if board[x][y] != '.':
                            if board[x][y] in s:
                                return False
                            s.add(board[x][y])
        return True
                
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_rows(board) and self.check_columns(board) and self.check_sub_boxes(board)
