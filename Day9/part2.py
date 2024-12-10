import numpy as np

disk_map_file = './Day9/input.txt'
with open(disk_map_file) as file:
    disk_map = np.array(list(file.readline())).astype('int64')

available_space = [disk_map[i] if i % 2 == 1 else 0 for i in range(len(disk_map))]
allocation = {}
moved_files = []
for j in range(len(disk_map) - 1, 0, -2):
    size = disk_map[j]
    ID = j // 2

    # finding if there is a free spot large enough for the file
    for i in range(len(available_space)):
        if i == j:
            break
        if available_space[i] >= size:
            available_space[i] -= size
            if i not in allocation:
                allocation[i] = []
            allocation[i] += [ID]
            moved_files += [ID]
            available_space[j] = size
            break

checksum = 0
k = 0
for i in range(len(disk_map)):
    # memory block
    if i % 2 == 0:
        ID = i //2
        size = disk_map[i]
        if ID not in moved_files:
            for _ in range(size):
                checksum += ID * k
                k += 1
        else:
            k += size

    # free space
    else:
        if i in allocation:
            for file in allocation[i]:
                size = disk_map[file * 2]
                for _ in range(size):
                    checksum += file * k
                    k += 1
        k += available_space[i]

print(checksum)


    