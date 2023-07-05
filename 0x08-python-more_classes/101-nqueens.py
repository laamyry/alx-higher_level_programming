#!/usr/bin/python3

"""The N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard. Write a program that solves
the N queens problem."""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for m in range(n)]
    [row.append(' ') for m in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for n in range(len(board)):
        for i in range(len(board)):
            if board[n][i] == "Q":
                solution.append([n, i])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for i in range(col + 1, len(board)):
        board[row][i] = "x"
    # X out all backwards spots
    for i in range(col - 1, -1, -1):
        board[row][i] = "x"
    # X out all spots below
    for n in range(row + 1, len(board)):
        board[n][col] = "x"
    # X out all spots above
    for n in range(row - 1, -1, -1):
        board[n][col] = "x"
    # X out all spots diagonally down to the right
    i = col + 1
    for n in range(row + 1, len(board)):
        if i >= len(board):
            break
        board[n][i] = "x"
        i += 1
    # X out all spots diagonally up to the left
    i = col - 1
    for n in range(row - 1, -1, -1):
        if i < 0:
            break
        board[n][i]
        i -= 1
    # X out all spots diagonally up to the right
    i = col + 1
    for n in range(row - 1, -1, -1):
        if i >= len(board):
            break
        board[n][i] = "x"
        i += 1
    # X out all spots diagonally down to the left
    i = col - 1
    for n in range(row + 1, len(board)):
        if i < 0:
            break
        board[n][i] = "x"
        i -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for i in range(len(board)):
        if board[row][i] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][i] = "Q"
            xout(tmp_board, row, i)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
