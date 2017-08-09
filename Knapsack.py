import sys
import numpy as np

with open(sys.argv[1]) as input1:
    num_items, capacity = input1.readline().strip().split(" ")
    weight = input1.readline().strip().split(" ")
    value = input1.readline().strip().split(" ")

capacity = int(capacity)
num_items = int(num_items)

# 2d list for Knapsack Tableau
ks = [[0 for x in range(capacity+1)] for x in range(num_items + 1)]

# Algorithm to fill Tableau
for i in range(1, num_items + 1):
    for w in range(capacity + 1):
        if int(weight[i-1]) <= w:
            ks[i][w] = max(ks[i-1][w], float(value[i-1]) + ks[i-1][w-int(weight[i-1])])
        else:
            ks[i][w] = ks[i-1][w]


A = np.array(ks)
np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
print("Tableau:")
print(A)

S = set()
i = num_items
j = capacity

# Creates set of Optimal items to fit in knapsack using tableau
while i >= 1 and j >= 1:
    while i >= 1 and ks[i-1][j] == ks[i][j]:
        i = i - 1
    S.add((i, int(weight[i-1]), float(value[i-1])))
    j = j - int(weight[i-1])
    i = i - 1

# the rest is just outputting the solutions
print("Maximum Capacity: W = " + str(capacity))
original = "Original Knapsack Items: [(1" + ", " + str(weight[0]) + \
               ", " + str(float(value[0])) + ")"

optVal = ks[num_items][capacity]
optWeight = 0

for item in S:
    optWeight += item[1]
for i in range(1, num_items):
    original = original + ", (" + str(i+1) + ", " + str(weight[i]) + \
               ", " + str(float(value[i])) + ")"

original = original + "]"
print(original)
print("Optimal Knapsack Items: " + str(S))
print("Optimal Weight: " + str(float(optWeight)))
print("Optimal Value: " + str(float(optVal)))