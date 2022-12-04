total_overlaps = 0
with open("sections.txt", "r") as sections:
    for line in sections:
        elf_a, elf_b = line.strip().split(",")
        elf_a = elf_a.split("-")
        elf_b = elf_b.split("-")
        elf_a = set(range(int(elf_a[0]), int(elf_a[1]) + 1))
        elf_b = set(range(int(elf_b[0]), int(elf_b[1]) + 1))
        # Part 1 condition
        # if len(elf_a - elf_b) == 0 or len(elf_b - elf_a) == 0:
        # Part 2 condition
        if len(elf_a - elf_b) < len(elf_a):
            total_overlaps += 1
print(total_overlaps)
        
