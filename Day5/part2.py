# finding out which udpates respect the rules

rules_and_updates_file = './Day5/input.txt'

rules = {}
updates = []
with open(rules_and_updates_file) as file:
    is_rules = True
    for line in file.readlines():
        if line == '\n':
            is_rules = False
            continue
        if is_rules:
            rule = line.split('\n')[0].split('|')
            nb1 = int(rule[0])
            nb2 = int(rule[1])
            if nb2 not in rules:
                rules[nb2] = []
            rules[nb2] += [nb1]
        else:
            updates += [line.split('\n')[0].split(',')]

middle_value = 0
for update in updates:
    ordered = False
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if int(update[i]) in rules and int(update[j]) in rules[int(update[i])]:
                ordered = True
                tmp = update[j]
                for k in range(j, i, -1):
                    update[k] = update[k - 1]
                update[i] = tmp
                j = i + 1

    if ordered:
        middle_value += int(update[len(update)//2])

print(middle_value)