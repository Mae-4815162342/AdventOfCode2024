import numpy as np

map_file = './Day10/input.txt'
map = []
with open(map_file) as file:
    for line in file.readlines():
        map += [list(line.split('\n')[0])]

map = np.array(map)

class Path:
    def __init__(self, position, height, map):
        self.position = position
        self.height = height
        
        #defining possible paths
        self.paths = []
        x, y = position
        if x - 1 >= 0:
            if map[x-1, y] != '.' and int(map[x-1, y]) == height + 1:
                self.paths += [Path((x - 1, y), height + 1, map)]

        if y - 1 >= 0:
            if map[x, y - 1] != '.' and int(map[x, y - 1]) == height + 1:
                self.paths += [Path((x, y - 1), height + 1, map)]

        if x + 1 < len(map):
            if map[x+1, y] != '.' and int(map[x+1, y]) == height + 1:
                self.paths += [Path((x + 1, y), height + 1, map)]

        if y + 1 < len(map[0]):
            if map[x, y + 1] != '.' and int(map[x, y + 1]) == height + 1:
                self.paths += [Path((x, y + 1), height + 1, map)]

    def is_leaf(self):
        return len(self.paths) == 0
    
def find_trail_ends(path, end_value):
    if path.is_leaf():
        return [path.position] if path.height == end_value else []
        
    trails_ends = [find_trail_ends(child, end_value) for child in path.paths]
    trails_ends = [trail for trail in trails_ends if len(trail) > 0]
    return np.concatenate(trails_ends) if len(trails_ends) > 0 else []

score = 0
for position in np.argwhere(map == '0'):
    trail = Path(position, 0, map)
    complete_trails = find_trail_ends(trail, 9)
    if len(complete_trails) > 0:
        unique_trails = np.array([complete_trails[0]])
        for end_pos in complete_trails:
            if end_pos[1] not in unique_trails[unique_trails[:, 0] == end_pos[0]][:, 1]:
                unique_trails = np.concatenate([unique_trails, [end_pos]])
        score += len(unique_trails)

print(score)


        
