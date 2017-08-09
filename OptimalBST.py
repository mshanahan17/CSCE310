import sys
import numpy as np


# simple node class for BST
class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


values = []
with open(sys.argv[1]) as input1:
    input1.readline()
    for line in input1:
        values.append(line.strip().split(" "))

values.sort(key=lambda x: x[0])

# initialize the cost matrix and root matrix
cost = [[0 for x in range(len(values) + 1)] for x in range(len(values) + 1)]
root_table = [[0] * len(values) for x in range(len(values))]

# fill in the default diagonal values
for i in range(len(values)):
    cost[i][i + 1] = float(values[i][1])
    root_table[i][i] = i + 1

# fills in the tableau values
for d in range(1, len(values)):
    for i in range(1, len(values) - d + 1):
        j = i + d
        min = 99
        for k in range(i, j + 1):
            q = float(cost[i - 1][k - 1]) + float(cost[k][j])
            if q < min:
                min = q
                root_table[i - 1][j - 1] = k
        sums = 0
        for pk in range(i - 1, j):
            sums += float(values[pk][1])
        cost[i - 1][j] = min + sums


np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
A = np.array(cost)
B = np.array(root_table)

# outputs the tableau
print('C =')
print(A)
print()
print('R =')
print(B)
print()

root = Node(root_table[0][len(values) - 1] - 1)
S = [(root, 0, len(values) - 1)]

# creates the BST using the completed root matrix
while S:
    u, i, j = S.pop()
    k = root_table[i][j] - 1
    if k < j:
        v = Node(root_table[k + 1][j] - 1, u)
        u.right = v
        S.append((v, k + 1, j))

    if i < k:
        v = Node(root_table[i][k - 1] - 1, u)
        u.left = v
        S.append((v, i, k - 1))


# traverses all nodes in the tree for output
def allKeys(d):
    to_visit = [d]
    while len(to_visit) > 0:
        x = to_visit.pop()
        if x is not None:
            print('Node:')
            print("   {}    {}".format("Key:", values[x.key][0]))
            print("   {}   {}".format("Prob:", values[x.key][1]))
            if x.parent is not None:
                print("   {} {}".format("Parent:", values[x.parent.key][0]))
            else:
                print("   Parent: %4s" % 'None')
            if x.left is not None:
                print("   {}   {}".format("Left:", values[x.left.key][0]))
            else:
                print("   Left: %6s" % 'None')
            if x.right is not None:
                print("   {}  {}".format("Right:", values[x.right.key][0]))
            else:
                print("   Right: %5s" % 'None')
            print()
        if x.left:
            to_visit.append(x.left)
        if x.right:
            to_visit.append(x.right)

allKeys(root)
