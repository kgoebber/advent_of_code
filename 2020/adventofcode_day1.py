import numpy as np


# # Advent of Code Day 1
# 
# Part 1

data = np.loadtxt('day1_input.txt').astype('int')

data_matrix = np.ones((data.size, data.size)).astype('int') * data

sum_matrix = data_matrix + data_matrix.T

row, col = np.where(sum_matrix == 2020)[0]

answer1 = data[row]*data[col]
print(f'Part 1: {answer1}')

# Part 2

for i in range(data.size):
    for j in range(i+1, data.size):
        for k in range(j+1, data.size):
            if (data[i] + data[j] + data[k] == 2020):
                answer2 = data[i]*data[j]*data[k]
                print(f'Part 2: {answer2}')

