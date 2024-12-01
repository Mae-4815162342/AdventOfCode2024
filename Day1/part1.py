import numpy as np
import re

location_file = './Day1/input.txt'

locations = []
with open(location_file) as file:
    line = file.readline()
    while line:
        values = re.sub('\n', '', line).split(' ')
        locations += [[float(values[0]), float(values[-1])]]
        line = file.readline()
locations = np.array(locations)

distance = 0
for i in range(len(locations)):
    index1 = np.argmin(locations[:, 0])
    index2 = np.argmin(locations[:, 1])
    distance += abs(locations[index1, 0] - locations[index2, 1])
    locations[index1, 0] = np.inf
    locations[index2, 1] = np.inf

print(distance)