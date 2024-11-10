#!/usr/bin/python3
"""
Solution to the N-Queens problem using backtracking.
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Recursive backtracking function to find solutions for the N-Queens problem.
    Args:
        r (int): The current row to place a queen.
        n (int): The size of the chessboard (N x N).
        cols (set): Set of columns where queens are already placed.
        pos (set): Set of positive diagonals where queens are placed.
        neg (set): Set of negative diagonals where queens are placed.
        board (list of lists): Represents the chessboard with queen placements.
    """
    # If all queens are placed, add the solution
    if r == n:
        # Convert board state to result format for printing
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:  # Queen is placed here
                    res.append([l, k])
        print(res)
        return

    # Try placing a queen in each column of the current row
    for c in range(n):
        # Skip columns and diagonals where a queen would be attacked
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        # Place queen at (r, c) and add to tracking sets
        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        # Move to the next row
        backtrack(r + 1, n, cols, pos, neg, board)

        # Backtrack: remove queen and reset tracking sets
        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Initializes the board and calls the backtracking function to solve the N-Queens problem.
    Args:
        n (int): Number of queens (and size of the chessboard).
    """
    # Initialize sets to track columns and diagonals
    cols = set()
    pos_diag = set()
    neg_diag = set()
    # Initialize the board with 0s, representing empty spaces
    board = [[0] * n for _ in range(n)]

    # Start backtracking from the first row
    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    # Parse command-line arguments
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        # Convert argument to integer and validate
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        # Solve the N-Queens problem
        nqueens(nn)
    except ValueError:
        # Handle non-integer input
        print("N must be a number")
        sys.exit(1)
