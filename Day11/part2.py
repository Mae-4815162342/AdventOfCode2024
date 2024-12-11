# Rules:
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

stones_file = './Day11/input.txt'
stones = {}
with open(stones_file) as file:
    tmp_stones = file.readline().split('\n')[0].split(' ')
    for stone in tmp_stones:
        if stone not in stones:
            stones[stone] = 1
        else:
            stones[stone] += 1

for blink in range(75):
    new_stones = {}
    for stone in stones.keys():
        nb_stone = stones[stone]
        if stone == '0':
            if '1' not in new_stones:
                new_stones['1'] = 0
            new_stones['1'] += nb_stone

        elif len(stone) % 2 == 0:
            pivot_point = len(stone)//2
            part1 = str(int(stone[:pivot_point]))
            part2 = str(int(stone[pivot_point:]))

            if part1 not in new_stones:
                new_stones[part1] = 0
            if part2 not in new_stones:
                new_stones[part2] = 0

            new_stones[part1] += nb_stone
            new_stones[part2] += nb_stone

        else:
            new_stone = str(int(stone) * 2024)
            if new_stone not in new_stones:
                new_stones[new_stone] = 0
            new_stones[new_stone] += nb_stone

    stones = new_stones

print(sum(list(stones.values())))