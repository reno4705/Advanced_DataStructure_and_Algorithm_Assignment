def solve_n_queens(N):
    def is_safe(board, row, col):
        # Check if no queen threatens the current cell
        # Check the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i, j = i - 1, j - 1
        
        # Check upper-right diagonal
        i, j = row, col
        while i >= 0 and j < N:
            if board[i][j] == 'Q':
                return False
            i, j = i - 1, j + 1
        
        return True

    def backtrack(board, row):
        if row == N:
            # Found a solution, add it to the results
            solutions.append([''.join(row) for row in board])
            return
        
        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'  # Backtrack

    solutions = []
    empty_board = [['.' for _ in range(N)] for _ in range(N)]
    backtrack(empty_board, 0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()

# Example usage for N = 4
N = 4
solutions = solve_n_queens(N)
print_solutions(solutions)
