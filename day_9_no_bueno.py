import numpy as np

def move_head(direction, steps, x, y):
    if direction == "U":
        y -= steps
    elif direction == "D":
        y += steps
    elif direction == "L":
        x -= steps
    elif direction == "R":
        x += steps
    else:
        raise ValueError(f"{direction} is not a valid direction.")
    return x, y


def move_tail_to_head(head_x, head_y, tail_x, tail_y):
    # Called on bad input --- different row and col
    if head_x != tail_x and head_y != tail_y:
        raise ValueError(f"head({head_x}, {head_y}) and tail({tail_x}, {tail_y}) not in same row/col.")
    # Called on bad input --- same spot
    if head_x == tail_x and head_y == tail_y:
        return tail_x, tail_y
    # Same column
    if head_x == tail_x:
        if head_y > tail_y:
            tail_y = head_y - 1
        else:
            tail_y = head_y + 1
    # Same row
    else:
        if head_x > tail_x:
            tail_x = head_x - 1
        else:
            tail_x = head_x + 1
    return tail_x, tail_y


def move_tail_diagonal(head_x, head_y, tail_x, tail_y):
    # They're not actually diagonal
    if head_x == tail_x or head_y == tail_y:
        raise ValueError(f"head({head_x}, {head_y}) and tail({tail_x}, {tail_y}) are in the same row/col.")
    # They're tooooo diagonal
    if abs(head_x - tail_x) > 1 and abs(head_y - tail_y) > 1:
        raise ValueError(f"head({head_x}, {head_y}) and tail({tail_x}, {tail_y}) can only differ by more than 1 in one direction.")
    # If they're just 1 away still by the diagonal
    if abs(head_x - tail_x) == 1 and abs(head_y - tail_y) == 1:
        pass
    else:
        tail_y += (head_y - tail_y) // abs(head_y - tail_y)
        tail_x += (head_x - tail_x) // abs(head_x - tail_x)     # Step once in proper direction
    return tail_x, tail_y


def get_tail_slice(x_1, y_1, x_2, y_2):
    # Called on bad input --- different row and col
    if x_1 != x_2 and y_1 != y_2:
        raise ValueError(f"head({x_1}, {y_1}) and tail({x_2}, {y_2}) not in same row/col.")
    # Same column
    if x_1 == x_2:
        return slice(min(y_1, y_2), max(y_1, y_2) + 1), x_1
    if y_1 == y_2:
        return y_1, slice(min(x_1, x_2), max(x_1, x_2) + 1)


if __name__ == "__main__":
    # Read Input
    FILE_NAME = "../resources/day_9.txt"
    moves_file = open(FILE_NAME, "r")
    moves = [(move.split()[0], int(move.split()[1])) for move in moves_file.readlines()]
    moves_file.close()

    # Setup the "board"
    board = np.zeros((1001, 1001))
    knots = []

    head_x, head_y = 500, 500
    tail_x, tail_y = 500, 500
    board[500,500] = 1   # Count start

    # Go time
    for direction, steps in moves:
        head_x, head_y = move_head(direction, steps, head_x, head_y)
        if head_x != tail_x and head_y != tail_y:
            tail_x, tail_y = move_tail_diagonal(head_x, head_y, tail_x, tail_y)
            board[tail_y, tail_x] = 1

        if head_x == tail_x or head_y == tail_y:
            new_tail_x, new_tail_y = move_tail_to_head(head_x, head_y, tail_x, tail_y)
            coordinate_slice = get_tail_slice(tail_x, tail_y, new_tail_x, new_tail_y)
            tail_x, tail_y = new_tail_x, new_tail_y
            board[coordinate_slice] = 1

    print(board)
    print(board.sum())
