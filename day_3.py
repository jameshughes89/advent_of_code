def priority(character):
    if character.islower():
        return ord(character) - 96
    else:
        return ord(character) - 64 + 26

def part_one(rucksacks):
    priority_total = 0
    for sack in rucksacks:
        sack_1 = set(sack[:len(sack)//2])
        sack_2 = set(sack[len(sack)//2:])
        sack_touching = sack_1.intersection(sack_2)
        priority_total += priority(sack_touching.pop())
    return priority_total
  
def part_two(rucksacks):
    priority_total = 0
    for i in range(0, len(rucksacks), 3):
        sack_1 = set(rucksacks[i])
        sack_2 = set(rucksacks[i + 1])
        sack_3 = set(rucksacks[i + 2])
        sack_touching = sack_1.intersection(sack_2).intersection(sack_3)
        priority_total += priority(sack_touching.pop())
    return priority_total

rucksacks = open("ruckshack.txt", "r").read().split("\n")
print(part_one(rucksacks))
print(part_two(rucksacks))
