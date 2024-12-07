# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three
import numpy as np

report_file = './Day2/input.txt'

nb_safe = 0
with open(report_file) as file:
    line = file.readline()

    while line:
        report = np.array(line.split('\n')[0].split(' ')).astype('int64')
        
        is_inc = (report[0] - report[1]) < 0
        skip = False

        for i in range(1, len(report)):
            dif = report[i] - report[i-1]
            if (is_inc and dif < 0) or (not is_inc and dif > 0):
                skip = True
                break
            if abs(dif) > 3 or dif == 0:
                skip = True
                break
        
        if not skip:
            nb_safe += 1

        line = file.readline()

print(nb_safe)