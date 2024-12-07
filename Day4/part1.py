# finds the occurences of the word in the crossword

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
word = 'XMAS'
word_count = 0
for i in range(len(crossword)):
    for j in range(len(crossword[0])):
        char = crossword[i,j]
        if char == word[0]:
            i_limit_neg = i - len(word) + 1 >= 0
            j_limit_neg = j - len(word) + 1 >= 0
            i_limit_pos = i + len(word) <= len(crossword)
            j_limit_pos = j + len(word) <= len(crossword[0])

            if i_limit_neg:
                word1 = ('').join([crossword[i - k, j] for k in range(len(word))])
                if word1 == word:
                    word_count += 1
            if j_limit_neg:
                word2 = ('').join([crossword[i, j - l] for l in range(len(word))])
                if word2 == word:
                    word_count += 1
            if i_limit_neg and j_limit_neg:
                word3 = ('').join([crossword[i - k, j - l] for k, l in zip(range(len(word)), range(len(word)))])
                if word3 == word:
                    word_count += 1
            if i_limit_pos:
                word4 = ('').join([crossword[i + k, j] for k in range(len(word))])
                if word4 == word:
                    word_count += 1
            if j_limit_pos:
                word5 = ('').join([crossword[i, j + l] for l in range(len(word))])
                if word5 == word:
                    word_count += 1
            if i_limit_pos and j_limit_pos:
                word6 = ('').join([crossword[i + k, j + l] for k, l in zip(range(len(word)), range(len(word)))])
                if word6 == word:
                    word_count += 1
            if i_limit_neg and j_limit_pos:
                word7 = ('').join([crossword[i - k, j + l] for k, l in zip(range(len(word)), range(len(word)))])
                if word7 == word:
                    word_count += 1
            if i_limit_pos and j_limit_neg:
                word8 = ('').join([crossword[i + k, j - l] for k, l in zip(range(len(word)), range(len(word)))])
                if word8 == word:
                    word_count += 1

print(word_count)



