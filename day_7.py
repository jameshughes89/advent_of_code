directories = []
sizes = {}

with open("commands.txt", "r") as commands:
    for command in commands:
        command = command.strip().split()
        if command[1] == "cd":
            # if moving up, need to add size to parent dir
            if command[2] == "..":
                contained = directories.copy()
                directories.pop()
                sizes[tuple(directories)] += sizes[tuple(contained)]
            else:
                directories.append(command[2])
        elif command[1] == "ls":
            # prep by adding dir to sizes dict
            sizes[tuple(directories)] = 0
        elif command[0] == "dir":
            # no one cares
            pass
        elif command[0].isnumeric():
            sizes[tuple(directories)] += int(command[0])
        else:
            print("wtf?")

# In case we end deep in the tree
# move back up the dir tree and add sizes to parents as we go
while len(directories) > 1:
    contained = directories.copy()
    directories.pop()
    sizes[tuple(directories)] += sizes[tuple(contained)]

# Part 1
running_total = 0
for k, v in sizes.items():
    if v <= 100000:
        running_total += v
print(running_total)



# Part 2
total_space = 70000000
needed_space = 30000000
current_space = total_space - sizes[("/",)]
must_free = needed_space - current_space

smallest_above_threshold = 999999999
for k, v in sizes.items():
    if v > must_free and v < smallest_above_threshold:
        smallest_above_threshold = v
print(smallest_above_threshold)
