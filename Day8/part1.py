import numpy as np

antenna_file = './Day8/input.txt'

map = []
with open(antenna_file) as file:
    for line in file.readlines():
        map += [list(line.split('\n')[0])]
map = np.array(map)

antinodes_map = np.copy(map)
frequences = np.unique(map)
frequences = np.delete(frequences, np.argwhere(frequences == '.'))

def compute_antinodes(x1, y1, x2, y2, max_x, max_y):
    distx, disty = x2 - x1, y2 - y1
    antinodes = []
    if x1 - distx < max_x and x1 - distx >= 0 and y1 - disty < max_y and y1 - disty >= 0:
        antinodes += [[x1 - distx, y1 - disty]]
    if x2 + distx < max_x and x2 + distx >= 0 and y2 + disty < max_y and y2 + disty >= 0:
        antinodes += [[x2 + distx, y2 + disty]]
    return antinodes

count = 0
for frequence in frequences:
    coordinates = np.argwhere(map == frequence)
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            antinodes = compute_antinodes(x1, y1, x2, y2, len(map), len(map[0]))
            for antinode in antinodes:
                if antinodes_map[antinode[0], antinode[1]] != '#':
                    antinodes_map[antinode[0], antinode[1]] = '#'
                    count += 1

print(count)