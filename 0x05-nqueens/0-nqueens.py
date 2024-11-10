#!/usr/bin/python3
import sys


def validate_input():
    """
    Validates the command-line input.
    Checks if the user provided exactly one argument, that it's an integer,
    and that the integer is 4 or greater.
    Prints an error message and exits with status 1 if validation fails.
    Returns:
        int: The size of the chessboard (N).
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Try converting the input argument to an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


def is_safe(board, row, col):
    """
    Checks if a queen can be placed at (row, col) on the board.
    Args:
        board (list): List representing the positions of queens by column index.
        row (int): The current row to place a queen.
        col (int): The current column to place a queen.
    Returns:
        bool: True if it's safe to place a queen at (row, col), False otherwise.
    """
    for i in range(row):
        # Check the same column and both diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """
    Recursively tries to place queens on the board using backtracking.
    Args:
        N (int): Size of the chessboard (N x N).
        row (int): The current row to attempt placing a queen.
        board (list): List representing the positions of queens by column index.
        solutions (list): Accumulates all possible solutions.
    """
    if row == N:
        # If all N queens are placed successfully, add solution to the list
        solutions.append([[i, board[i]] for i in range(N)])
        return

    # Attempt to place a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col):
            # Place the queen at (row, col)
            board[row] = col
            # Move to the next row with the updated board
            solve_nqueens(N, row + 1, board, solutions)


def print_solutions(solutions):
    """
    Prints all solutions in the specified format.
    Args:
        solutions (list): List of solutions, where each solution is a list
                          of [row, col] positions of queens.
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Validate input and get the size of the chessboard
    N = validate_input()
    # Initialize the board with -1 (no queens placed initially)
    board = [-1] * N
    # List to hold all possible solutions
    solutions = []
    # Solve the N Queens problem and store solutions
    solve_nqueens(N, 0, board, solutions)
    # Print each solution in the required format
    print_solutions(solutions)
