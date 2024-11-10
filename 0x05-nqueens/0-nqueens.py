#!/usr/bin/python3
"""
Solution to the N Queens problem.
"""

import sys


def backtrack(row, n, cols, pos_diag, neg_diag, board):
    """
    Recursive backtrack function to find all solutions.
    """
    if row == n:
        # Collect solution as list of coordinates
        solution = [[i, board[i].index(1)] for i in range(n)]
        print(solution)
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
            continue

        # Place queen and mark attacks
        cols.add(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)
        board[row][col] = 1

        # Move to next row
        backtrack(row + 1, n, cols, pos_diag, neg_diag, board)

        # Remove queen and unmark attacks
        cols.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Initializes the N Queens problem and starts the backtracking process.
    """
    board = [[0] * n for _ in range(n)]
    backtrack(0, n, set(), set(), set(), board)


if __name__ == "__main__":
    # Argument validation
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Execute the N Queens solution with valid input
    nqueens(n)
