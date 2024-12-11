import numpy as np

map_file = './Day6/input.txt'
map = []
with open(map_file) as file:
    for line in file.readlines():
        map += [list(line.split('\n')[0])]

map = np.array(map)

rules = {
        '^':[-1, 0, '>'],
        '>':[0, 1, 'v'],
        'v':[1, 0, '<'],
        '<':[0, -1, '^']
    }

def get_guard_position(map):
    """Retrieves guard position"""
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i, j] in ['^', 'v', '<', '>']:
                return i, j
    return -1, -1

def move_guard(x, y, map):
    """Moves a guard of one box. Rotates the guard if necessary. If the guard leaves the map, return None. Else the new coordinates of the guard."""
    rule = rules[map[x, y]]

    # checking if the map is leaved by the next move
    if x + rule[0] < 0 or x + rule[0] >= len(map) or y + rule[1] < 0 or y + rule[1] >= len(map[0]):
        return None, None

    # rotating
    while map[x + rule[0], y + rule[1]] == '#':
        map[x, y] = rule[2]
        rule = rules[rule[2]]

    # moving forward
    map[x + rule[0], y + rule[1]] = map[x, y]
    map[x, y] = '.'
    return x + rule[0], y + rule[1]

def check_loop(x, y, global_map):
    map = np.copy(global_map) 
    coordinates_list = []
    x_tmp, y_tmp = move_guard(x, y, np.copy(map))
    if x_tmp and y_tmp:
        map[x_tmp, y_tmp] = "#"
    i = 0
    while x and y and i < 10000:
        coordinates_list += [(x, y, map[x, y])]
        x, y = move_guard(x, y, map)
        i += 1
        if (x, y, map[x, y]) in coordinates_list:
            return True
    return False


x, y = get_guard_position(map)
count = 0
obstacle_global_map = np.copy(map)
while x and y:
    x, y = move_guard(x, y, map)

    tmp_x, tmp_y = x, y

    if tmp_x and tmp_y:
        tmp_rule = rules[map[tmp_x, tmp_y]]
        is_loop = check_loop(tmp_x, tmp_y, map)
        if is_loop and obstacle_global_map[tmp_x + tmp_rule[0], tmp_y + tmp_rule[1]] != 'O':
            count += 1
            obstacle_global_map[tmp_x, tmp_y]

with open('./Day6/result_file.txt', 'w') as file:
    lines = '\n'.join([''.join(line) for line in obstacle_global_map])
    file.writelines(lines)
print(count)