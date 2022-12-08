trees_file = open("trees.txt", "r")
trees = [list(map(int, list(row.strip()))) for row in trees_file.readlines()]
trees_file.close()

# Part 1
def walk_row(tree_height, row, trees, walk):
    for i in walk:
        if trees[row][i] >= tree_height:
            return 0
    return 1

def walk_col(tree_height, col, trees, walk):
    for i in walk:
        if trees[i][col] >= tree_height:
            return 0
    return 1

def down_tree_lines(row, col, trees):
    tree_height = trees[row][col]
    is_visible = 0
    # Check row back
    is_visible += walk_row(tree_height, row, trees, range(col-1, -1, -1))
    # Check row forward
    is_visible += walk_row(tree_height, row, trees, range(col+1, len(trees), 1))
    # Check col up
    is_visible += walk_col(tree_height, col, trees, range(row-1, -1, -1))
    # check col down
    is_visible += walk_col(tree_height, col, trees, range(row+1, len(trees), 1))
    return min(1, is_visible)

# Assumes square
trees_seen = len(trees) * 4 - 4 # -4 because counting each corner 2x
for row in range(1, len(trees) - 1):
    for col in range(1, len(trees) - 1):
        trees_seen += down_tree_lines(row, col, trees)

        
print(trees_seen)

# Part 2
def walk_row_score(tree_height, row, trees, walk):
    seen = 0
    for i in walk:
        if trees[row][i] < tree_height:
            seen += 1
        if trees[row][i] >= tree_height:
            seen += 1
            return seen
    return seen

def walk_col_score(tree_height, col, trees, walk):
    seen = 0
    for i in walk:
        if trees[i][col] < tree_height:
            seen += 1
        if trees[i][col] >= tree_height:
            seen +=1
            return seen
    return seen


def down_tree_lines_score(row, col, trees):
    tree_height = trees[row][col]
    score = 1
    # Check row back
    score *= walk_row_score(tree_height, row, trees, range(col-1, -1, -1))
    # Check row forward
    score *= walk_row_score(tree_height, row, trees, range(col+1, len(trees), 1))
    # Check col up
    score *= walk_col_score(tree_height, col, trees, range(row-1, -1, -1))
    # check col down
    score *= walk_col_score(tree_height, col, trees, range(row+1, len(trees), 1))
    return score

# Assumes square
# Also, edge trees have a 0, so their score is 0
best_score = 0
for row in range(1, len(trees) - 1):
    for col in range(1, len(trees) - 1):
        tree_score = down_tree_lines_score(row, col, trees)
        if tree_score > best_score:
            best_score = tree_score


        
print(best_score)
