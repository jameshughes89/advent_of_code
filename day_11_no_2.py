def make_operation(operation_line):
    if operation_line[4] == "+":
        op = add
    elif operation_line[4] == "*":
        op = mul
    else:
        print("Maybe this atters in part 2")
    if operation_line[3] == "old":
        if operation_line[5] == "old":
            return lambda old : op(old, old)
        else:
            return lambda old : op(old, int(operation_line[5]))
    else:
        print("Maybe this matters for part 2")

def make_throw(monkey_mood):
    return lambda x: int(monkey_mood[4][5]) if x % int(monkey_mood[3][3]) == 0 else int(monkey_mood[5][5])
  
  from IPython.core.async_helpers import inspect
from operator import add, mul
from copy import deepcopy
with open("day_11.txt", "r") as monkey_file:
    monkey_data = monkey_file.read().split("\n\n")

monkeys = []
for monkey_mood in monkey_data:
    monkey_mood = [mood.split() for mood in monkey_mood.split("\n")]
    monkey = {}
    monkey["number"] = int(monkey_mood[0][1][:-1])
    monkey["items"] = [int(item.replace(",","")) for item in monkey_mood[1][2:]]
    monkey["operation"] = make_operation(monkey_mood[2])
    monkey["throw"] = make_throw(monkey_mood)
    monkeys.append(monkey)

inspections = [0] * len(monkeys)

initial_monkeys = deepcopy(monkeys)

for round in range(20):
    for i, monkey in enumerate(monkeys):
        while(len(monkey["items"]) > 0):
            inspections[i] += 1
            item = monkey["items"].pop(0)
            item = monkey["operation"](item)
            #if (item**0.5) * (item**0.5) == item:
            #    item = int(item**0.5)
            item = item // 3
            throw_to = monkey["throw"](item)
            monkeys[throw_to]["items"].append(item)

print(inspections)
inspections.sort()
print(inspections[-1] * inspections[-2])
