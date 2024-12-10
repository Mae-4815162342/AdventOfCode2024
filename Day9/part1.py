
disk_map_file = './Day9/input.txt'
with open(disk_map_file) as file:
    disk_map = list(file.readline())

checksum = 0
i = 0
j = len(disk_map) - 1
k = 0
while i <= j:
    size = int(disk_map[i])
    # memory block
    if i % 2 == 0:
        ID = i // 2
        for _ in range(size):
            checksum += k * ID
            k += 1
        i += 1

    # free space
    else:
        size_end = int(disk_map[j])
        if j % 2 == 1:
            j -= 1
            continue
        ID = j // 2
        while size > 0 and size_end > 0:
            checksum += k * ID
            k += 1
            size -= 1
            size_end -=1
        
        # the end hasn't been completly transfered
        if size_end > 0:
            disk_map[j] = size_end
            i += 1
        # the free space is not completely filled
        elif size > 0:
            disk_map[i] = size
            j -= 1
        else:
            i += 1
            j -=1

print(checksum)


    