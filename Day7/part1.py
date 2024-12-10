import numpy as np
calibration_file = './Day7/input.txt'

calibrations = {}
with open(calibration_file) as file:
    for line in file.readlines():
        values = line.split('\n')[0].split(':')
        calibrations[int(values[0])] = np.array(values[1].split(' ')[1:]).astype('int64')

class Node:
    def __init__(self, value, list):
        self.value = value
        if len(list) > 1:
            self.multiply = Node(value * list[0], list[1:])
            self.add = Node(value + list[0], list[1:])
        elif len(list) == 1:
            self.multiply = Node(value * list[0], [])
            self.add = Node(value + list[0], [])
        else:
            self.multiply = None
            self.add = None

    def is_leaf(self):
        return self.multiply == None and self.add == None
    
def explore_tree(tree, to_find):
    if tree.is_leaf():
        return tree.value == to_find
    return explore_tree(tree.multiply, to_find) or explore_tree(tree.add, to_find)

count = 0
for to_find in calibrations.keys():
    list = calibrations[to_find]
    if len(list) > 1:
        tree = Node(list[0], list[1:])
        if explore_tree(tree, to_find):
            count += to_find
    else:
        if list[0] == to_find:
            count += to_find

print(count)
