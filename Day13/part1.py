machines_file = './Day13/input.txt'
machines = {}
with open(machines_file) as file:
    current_A = []
    current_B = []
    current_prize = []
    id = 1
    for line in file.readlines():
        if line == '\n':
            machines[id] = [current_A, current_B, current_prize]
            current_A = []
            current_B = []
            current_prize = []
            id += 1
        else:
            values = line.split('\n')[0].split(' ')
            X = int(values[-2][2:-1])
            Y = int(values[-1][2:])
            match values[0]:
                case "Button":
                    match values[1]:
                        case "A:":
                            current_A = [X, Y]
                        case "B:":
                            current_B = [X, Y]
                case "Prize:":
                    current_prize = [X, Y]
    machines[id] = [current_A, current_B, current_prize]

def minimize_price(A, B, prize, nA, nB):
    if nA > 100 or nB > 100:
        return False, -1, -1
    # Stop cases
    if prize[0] == 0 and prize[1] == 0:
        return True, nA, nB
    if prize[0] < 0 or prize[1] < 0:
        return False, -1, -1
    if (prize[0] - B[0] < 0 or prize[1] - B[1] < 0) and (prize[0] - A[0] < 0 or prize[1] - A[1] < 0):
        return False, -1, -1

    # Recursion priorizing B button
    kB = min(prize[0]//B[0], prize[1]//B[1])
    kA = min((prize[0] -  kB*B[0])//A[0], (prize[1] -  kB*B[1])//A[1])
    validB, new_nA, new_nB = minimize_price(A, B, [prize[0] - kB*B[0] - kA*A[0], prize[1] - kB*B[1] - kA*A[1]], nA + kA, nB + kB)
    if validB:
       return validB, new_nA, new_nB
    return minimize_price(A, B, [prize[0] - A[0], prize[1] - A[1]], nA + 1, nB)

tokens = 0
for id in machines.keys():
    A, B, prize = machines[id]
    valid_combination, nA, nB = minimize_price(A, B, prize, 0, 0)
    if valid_combination:
        print(id)
        tokens += nA*3 + nB

print(tokens)