# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-27-2022
# Description: Takes a list of integers that represents a row in a puzzle. Returns True if puzzle is able to be solved
# in that row. Returns False if otherwise.

def row_tracker(row, index, memo):
    """
    Helper function to that uses recursion to keep track of solvable and insolveable conditions by returning either True
     or False. Also keeps track of the indices that have been visited.
     """
    right_side = False
    left_side = False
    row_size = len(row)
    position = row[index]

    if index + 1 > row_size or index < 0 or memo[index]:
        return False
    if row_size == row[index] or index + 1 == row_size:
        return True

    memo[index] = 1

    if index + position < row_size:
        right_side = row_tracker(row, position + index, memo)
    if index - position > 0:
        left_side = row_tracker(row, index - position, memo)
    if right_side is True or left_side is True:
        return True
    else:
        return False


def add_token(row, memo):
    """Represents the 0 token needed to be added at end of the puzzle."""
    range_row = range(len(row))
    for _ in range_row:
        memo.append(0)


def row_puzzle(row):
    """
    Calls add_token to generate token to be inserted at end of list. Calls the row_tracker function as a helper
    function. Returns True if row puzzle is solvable for given row. Returns false if the puzzle is not solvable.
    """
    memo = []
    add_token(row, memo)
    return row_tracker(row, 0, memo)


