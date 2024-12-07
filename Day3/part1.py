# recognize mul(X,Y) instructions in the corrupted memory

memory_file='./Day3/input.txt'

sequence = ''
with open(memory_file) as file:
    sequence = ('\n').join(file.readlines())

instructions = sequence.split('mul(')

value = 0

for instruction in instructions:
    numbers = instruction.split(')')[0]
    splitted_numbers = numbers.split(',')
    if len(splitted_numbers) < 2 or not splitted_numbers[0].isnumeric() or not splitted_numbers[1].isnumeric():
        continue

    if int(splitted_numbers[0]) > 999 or int(splitted_numbers[1]) > 999:
        continue

    value += int(splitted_numbers[0]) * int(splitted_numbers[1])

print(value)



