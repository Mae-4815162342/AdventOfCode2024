# find the occurences of the word MAS crossed with itself
import numpy as np
import re

crossword_file = './Day4/input.txt'

crossword = []
with open(crossword_file) as file:
    line = file.readline()
    while line:
        crossword += [list(re.sub('\n', '', line))]
        line = file.readline()
crossword = np.array(crossword)

cross_count = 0
for i in range(1,len(crossword) - 1):
    for j in range(1, len(crossword[0]) - 1):
        char = crossword[i,j]
        if char == 'A':
            letter1 = crossword[i - 1, j - 1]
            letter2 = crossword[i - 1, j + 1]
            letter3 = crossword[i + 1, j - 1]
            letter4 = crossword[i + 1, j + 1]

            if (letter1 + letter4 == 'MS' or letter4 + letter1 == 'MS') and (letter2 + letter3 == 'MS' or letter3 + letter2 == 'MS'):
                cross_count += 1

print(cross_count)



