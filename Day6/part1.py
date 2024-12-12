# find the guard's path throughout the lab. 
# Every time the gards meets an obstacle, they turn 90 right until they can advance again.

import numpy as np

map_file = './Day6/input.txt'

map = []
with open(map_file) as file:
    for line in file.readlines():
        map += [list(line.split('\n')[0])]

map = np.array(map)

# finding guard position
x, y = 0, 0
up_list = np.argwhere(map == '^')
if len(up_list) > 0:
    x, y = up_list[0][0], up_list[0][1]
right_list = np.argwhere(map == '>')
if len(right_list) > 0:
    x, y = right_list[0][0], right_list[0][1]
down_list = np.argwhere(map == 'v')
if len(down_list) > 0:
    x, y = down_list[0][0], down_list[0][1]
left_list = np.argwhere(map == '<')
if len(left_list) > 0:
    x, y = left_list[0][0], left_list[0][1]

# moving rules {facing: [i, j, next_facing]}
rules = {
    '^': [-1, 0, '>'],
    '>': [0, 1, 'v'],
    'v': [1, 0, '<'],
    '<': [0, -1, '^'],
}

count = 1
while True:
    rule = rules[map[x, y]]
    if x + rule[0] < 0 or x + rule[0] >= len(map) or y + rule[1] < 0 or y + rule[1] >= len(map[0]):
        break

    if map[x + rule[0], y + rule[1]] == '#':
        map[x, y] = rule[2]
        continue
    
    if map[x + rule[0], y + rule[1]] == '.':
        count += 1
    map[x + rule[0], y + rule[1]] = map[x, y]
    map[x, y] = 'X'
    x, y = x + rule[0], y + rule[1]

print(count)
