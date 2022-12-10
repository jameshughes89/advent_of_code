with open("day_10.txt", "r") as ops:
    ops = [op.split() for op in ops]


x_register = 1
add_next = 0
clock_tick = 0
program_counter = 0
signal_clock = 20
line_end = 40
signals = []
crt_output = ""
while program_counter < len(ops):
    # Drawing bit
    if abs(x_register - (clock_tick % 40)) < 2:
        crt_output += "#"
    else:
        crt_output += "."
    # Op bit
    clock_tick += 1
    op = ops[program_counter]
    if clock_tick % signal_clock == 0:
        signals.append(x_register * clock_tick)
        signal_clock += 40
    if op[0] == "noop":
        program_counter += 1
    elif op[0] == "addx":
        if add_next == 0:
            add_next = int(op[1])
        else:
            x_register += add_next
            add_next = 0
            program_counter += 1
    else:
        print("Something weird")
    if clock_tick % line_end == 0:
        crt_output += "\n"

print(signals)
print(sum(signals))
print(crt_output)
