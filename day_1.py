def build_sum_calories(calories_list, calories_index, elf_list, elf_index):
  elf_list = elf_list.copy()
  # Base case --- end of list
  if calories_index == len(calories_list):
    return elf_list
  calories_current = calories_list[calories_index]
  # If we're not on a "blank line"
  if calories_current != -1:
    # If there is no data for the current elf, append
    if elf_index == len(elf_list):
      elf_list.append(calories_current)
    # If there is data for the current elf, just add to it's total
    else:
      elf_list[elf_index] += calories_current
    calories_index += 1
  # If it is a "blank line", go to next elf
  else:
    elf_index += 1
    calories_index += 1
  return build_sum_calories(calories_list, calories_index, elf_list, elf_index)

#elf_totals = build_sum_calories(calories_list, 0, [], 0)




calories_list = []
with open("calories.txt", "r") as calories_file:
  for line in calories_file:
    line = line.strip()
    if line.isnumeric():
      calories_list.append(int(line))
    else:
      calories_list.append(-1)
      
calories_index = 0
elf_index = 0
elf_list = []

for current_calories in calories_list:
  if current_calories != -1:
    if elf_index == len(elf_list):
      elf_list.append(current_calories)
    else:
      elf_list[elf_index] += current_calories
  else:
    elf_index += 1
  calories_index += 1

print(elf_list)
print(np.argmax(elf_list))
print(sum(np.sort(elf_list)[-3:]))
print(len(elf_list))
print(calories_list.count(-1))
