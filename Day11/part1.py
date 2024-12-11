# Rules:
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

stones_file = './Day11/input.txt'
stones = []
with open(stones_file) as file:
    stones = file.readline().split('\n')[0].split(' ')

for blink in range(25):
    new_stones = []
    for stone in stones:
        if int(stone) == 0:
            new_stones += ['1']
        elif len(stone) % 2 == 0:
            part1 = str(int(stone[:len(stone)//2]))
            part2 = str(int(stone[len(stone)//2:]))
            new_stones += [part1, part2]
        else:
            new_stones += [str(int(stone)*2024)]
    stones = new_stones

print(len(stones))