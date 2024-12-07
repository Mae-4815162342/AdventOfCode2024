# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three
# If by deleting one level, an unsafe report can be safe, it must be counted as so
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
            if (is_inc and dif < 0) or (not is_inc and dif > 0) or abs(dif) > 3 or dif == 0:
                skip = True
                break

        if not skip:
            nb_safe += 1

        # dampening
        else:
            for k in range(len(report)):
                new_report = [report[j] for j in range(len(report)) if j != k]
                is_inc = (new_report[0] - new_report[1]) < 0
                skip = False
                for i in range(1, len(new_report)):
                    dif = new_report[i] - new_report[i-1]
                    if (is_inc and dif < 0) or (not is_inc and dif > 0) or abs(dif) > 3 or dif == 0:
                        skip = True
                        break
                if not skip:
                    nb_safe += 1
                    break
                

        line = file.readline()

print(nb_safe)