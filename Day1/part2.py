import numpy as np
import re

location_file = './Day1/input.txt'

locations = []
with open(location_file) as file:
    line = file.readline()
    while line:
        values = re.sub('\n', '', line).split(' ')
        locations += [[int(values[0]), int(values[-1])]]
        line = file.readline()
locations = np.array(locations)

similarity = 0
for i in range(len(locations)):
    current_value = locations[i, 0]
    occurences = len(locations[locations[:, 1] == current_value])
    similarity += current_value * occurences
print(similarity)