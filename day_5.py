import copy

def lift_up(stack, n):
    return stack[n:], stack[:n]

def lift_down(stack, moved):
    return moved[::-1] + stack

def lift_down_9001(stack, moved):
    return moved + stack
  
  
# STFU --- deal with it  
some_string = """        [G]         [D]     [Q]    
[P]     [T]         [L] [M] [Z]    
[Z] [Z] [C]         [Z] [G] [W]    
[M] [B] [F]         [P] [C] [H] [N]
[T] [S] [R]     [H] [W] [R] [L] [W]
[R] [T] [Q] [Z] [R] [S] [Z] [F] [P]
[C] [N] [H] [R] [N] [H] [D] [J] [Q]
[N] [D] [M] [G] [Z] [F] [W] [S] [S]"""
stacks_data = some_string.split("\n")

stacks = [[], [], [], [], [], [], [], [], []] 
for row in stacks_data:
    index = 0
    for col in range(1, len(row), 4):
        if row[col] != " ":
            stacks[index].append(row[col])
        index += 1
print(stacks)

with open("moves.txt", "r") as moves:
    for move in moves:
        stacks = copy.deepcopy(stacks)
        move = move.split()
        n = int(move[1])
        from_stack = int(move[3]) - 1
        to_stack = int(move[5]) - 1
        stacks[from_stack], move_me = lift_up(stacks[from_stack], n)
        #stacks[to_stack] = lift_down(stacks[to_stack], move_me)
        stacks[to_stack] = lift_down_9001(stacks[to_stack], move_me)

for stack in stacks:
    print(stack[0])
