class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [-1] * n
        all_sol = []
        result = []
        def is_safe(queen, col):
            for prev_queen in range(queen):
                prev_col = board[prev_queen]
                if prev_col == col:
                    return False
                
                if abs(prev_col-col) == abs(prev_queen-queen):
                    return False
            return True
        
        def backtrack(queen):
            if queen == n:
                formatted_board = []
                for col in board:
                    row_str = "." * col + "Q" + "." * (n - col - 1)
                    formatted_board.append(row_str)
                all_sol.append(formatted_board)
                return
            
            for col in range(n):
                if is_safe(queen, col):
                    board[queen] = col
                    backtrack(queen+1)
                    board[queen] = -1
                else:
                    continue
            return all_sol
        backtrack(0)
        return all_sol
