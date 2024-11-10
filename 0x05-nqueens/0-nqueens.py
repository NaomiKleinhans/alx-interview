#!/usr/bin/python3
"""
Solution to the N Queens problem
"""

import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Recursive backtrack function to find all solutions.
    Args:
        r (int): Current row being filled with a queen.
        n (int): Size of the board (n x n).
        cols (set): Set of columns currently under attack.
        pos (set): Set of positive diagonals under attack.
        neg (set): Set of negative diagonals under attack.
        board (list of lists): Current board configuration.
    """
    if r == n:
        # Collect solution as list of coordinates
        solution = [[i, row.index(1)] for i, row in enumerate(board)]
        print(solution)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        # Place queen and mark attacks
        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        # Move to next row
        backtrack(r + 1, n, cols, pos, neg, board)

        # Remove queen and unmark attacks
        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Initializes the N Queens problem and starts the backtracking process.
    Args:
        n (int): The size of the board (n x n).
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


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

    # Run N Queens with valid input
    nqueens(n)
