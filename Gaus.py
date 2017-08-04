import sys

# reads in files and creates an n X n+1 sized array
with open(sys.argv[1]) as input1:
    num_func = int(input1.readline())
    matrix = [[0 for i in range(num_func + 1)] for j in range(num_func)]
    for line in range(num_func):
        values = input1.readline().strip().split(" ")
        for i in range(0, num_func):
            matrix[line][i] = float(values[i])
    b_vals = input1.readline().strip().split(" ")
    for i in range(num_func):
        matrix[i][num_func] = float(b_vals[i])

# upper triangle matrix algorithm
for i in range(len(matrix) - 1):
    pivot_row = i
    for j in range(i + 1, len(matrix)):
        if abs(matrix[j][i]) > abs(matrix[pivot_row][i]):
            pivot_row = j
    for k in range(i, len(matrix) + 1):
        temp = matrix[i][k]
        matrix[i][k] = matrix[pivot_row][k]
        matrix[pivot_row][k] = temp
    for j in range(i + 1, len(matrix)):
        t = matrix[j][i] / matrix[i][i]
        for k in range(i, len(matrix) + 1):
            matrix[j][k] = matrix[j][k] - matrix[i][k] * t

# checks last matrix row if solution exists
count = 0
for i in range(len(matrix) + 1):
    if matrix[len(matrix) - 1][i] == 0:
        count += 1
if count == len(matrix):
    print("Inconsistent")
    sys.exit(0)
if count == len(matrix) + 1:
    print("Indeterminate")
    sys.exit(0)

# Better gausian elimination to create solution vector
vector = [0 for i in range(num_func)]
for i in range(len(matrix)-1, -1, -1):
    t = matrix[i][len(matrix)]
    for j in range(i + 1, len(matrix)):
        t = t - vector[j] * matrix[i][j]
    vector[i] = t / matrix[i][i]

print(", ".join("%s" % round(f, 4) for f in vector))





