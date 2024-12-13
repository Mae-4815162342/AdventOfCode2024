import numpy as np

machines_file = './Day13/input.txt'
machines = {}
with open(machines_file) as file:
    current_A = []
    current_B = []
    current_prize = []
    id = 1
    for line in file.readlines():
        if line == '\n':
            machines[id] = [np.array(current_A), np.array(current_B), np.array(current_prize)]
            current_A = []
            current_B = []
            current_prize = []
            id += 1
        else:
            values = line.split('\n')[0].split(' ')
            X = float(values[-2][2:-1])
            Y = float(values[-1][2:])
            match values[0]:
                case "Button":
                    match values[1]:
                        case "A:":
                            current_A = [X, Y]
                        case "B:":
                            current_B = [X, Y]
                case "Prize:":
                    X = int("10000000000000" + values[-2][2:-1])
                    Y = int("10000000000000" + values[-1][2:])
                    # X = int(values[-2][2:-1])
                    # Y = int(values[-1][2:])
                    current_prize = [X, Y]
    machines[id] = [np.array(current_A), np.array(current_B), np.array(current_prize)]

tokens = 0
for id in machines.keys():
    A, B, prize = machines[id]
    matrix = np.array([A, B]).T
    inv = np.linalg.inv(matrix)
    K = inv @ prize.T
    # possible values for kA and kB are kA + 1 and kB + 1 as the computation above gives underestimated values
    if id == 3:
        print(K)
    K = np.round(K)
    if id == 3:
        print(K)
    result = matrix @ K
    if id == 3:
        print(result, prize)
    if result[0] == prize[0] and result[1] == prize[1]:
        tokens += int(K[0]) * 3 + int(K[1])

print(int(tokens))