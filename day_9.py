import numpy as np

# Read Input
FILE_NAME = "../resources/day_9.txt"
moves_file = open(FILE_NAME, "r")
moves = [(move.split()[0], int(move.split()[1])) for move in moves_file.readlines()]
moves_file.close()

# Setup the "board"
board = np.zeros((1001, 1001))
head_x, head_y = 500, 500
tail_x, tail_y = 500, 500
board[500,500] = 1   # Count start

# Go time
for direction, steps in moves:
    for _ in range(steps):
        if direction == "U":
            head_y -= 1
        elif direction == "D":
            head_y += 1
        elif direction == "L":
            head_x -= 1
        elif direction == "R":
            head_x += 1
        else:
            print("ya dun effed up  >-|-D: ")

        # Diagonal
        if (abs(head_x - tail_x) == 1 and abs(head_y - tail_y) > 1) or (abs(head_x - tail_x) > 1 and abs(head_y - tail_y) == 1):
            tail_x += (head_x - tail_x)//abs(head_x - tail_x)
            tail_y += (head_y - tail_y) // abs(head_y - tail_y)
        # Moving along a row
        elif abs(head_x - tail_x) == 2 and abs(head_y - tail_y) == 0:
            tail_x += (head_x - tail_x)//abs(head_x - tail_x)
        # Moving along a column
        elif abs(head_x - tail_x) == 0 and abs(head_y - tail_y) == 2:
            tail_y += (head_y - tail_y) // abs(head_y - tail_y)
        else:
            pass
        board[tail_y, tail_x] = 1

print(board)
print(board.sum())



# Setup the "board"
board = np.zeros((1001, 1001))
knots = []
for i in range(10):
    knots.append((500, 500))

board[knots[9]] = 1   # Count start

# Go time
for direction, steps in moves:
    for _ in range(steps):
        head_x, head_y = knots[0]

        if direction == "U":
            head_y -= 1
        elif direction == "D":
            head_y += 1
        elif direction == "L":
            head_x -= 1
        elif direction == "R":
            head_x += 1
        else:
            print("ya dun effed up  >-|-D: ")
        knots[0] = (head_x, head_y)

        for i in range(1, 10):
            head_x, head_y = knots[i-1]
            tail_x, tail_y = knots[i]

            # Diagonal
            if (abs(head_x - tail_x) == 1 and abs(head_y - tail_y) > 1) \
                    or (abs(head_x - tail_x) > 1 and abs(head_y - tail_y) == 1) \
                    or (abs(head_x - tail_x) > 1 and abs(head_y - tail_y) > 1) \
                    or (abs(head_x - tail_x) > 1 and abs(head_y - tail_y) > 1):
                tail_x += (head_x - tail_x)//abs(head_x - tail_x)
                tail_y += (head_y - tail_y)//abs(head_y - tail_y)
            # Moving along a row
            elif abs(head_x - tail_x) == 2 and abs(head_y - tail_y) == 0:
                tail_x += (head_x - tail_x)//abs(head_x - tail_x)
            # Moving along a column
            elif abs(head_x - tail_x) == 0 and abs(head_y - tail_y) == 2:
                tail_y += (head_y - tail_y)//abs(head_y - tail_y)
            else:
                pass
            knots[i] = (tail_x, tail_y)
            if i == 9:
                board[tail_y, tail_x] = 1

print(board)
print(board.sum())
