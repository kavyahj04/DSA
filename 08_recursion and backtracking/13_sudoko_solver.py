class Solution:
    def isValid(self, board, row, col, num):

        for i in range(9):

            # Check row
            if board[row][i] == num:
                return False

            # Check column
            if board[i][col] == num:
                return False

            # Check 3 x 3 box
            boxRow = 3 * (row // 3) + i // 3
            boxCol = 3 * (col // 3) + i % 3

            if board[boxRow][boxCol] == num:
                return False

        return True

    def solve(self, board):

        for row in range(9):
            for col in range(9):

                if board[row][col] == '.':

                    for num in "123456789":

                        if self.isValid(board, row, col, num):

                            # Choose
                            board[row][col] = num

                            # Explore
                            if self.solve(board):
                                return True

                            # Backtrack
                            board[row][col] = '.'

                    return False

        return True
    
    def solveSudoku(self, board: list[list[str]]) -> None:
        self.solve(board)
    
    