import sys


def lcs(str1, length):

    matrix = [[0 for x in range(length + 1)] for x in range(length + 1)]
    rev = str1[::-1]

    for i in range(length + 1):
        for j in range(length + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif str1[i - 1] == rev[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    index = matrix[length][length]
    sub = [""] * index

    i = length
    j = length
    while i > 0 and j > 0:
        if str1[i - 1] == rev[j - 1]:
            sub[index - 1] = str1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif matrix[i - 1][j] > matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("Length: " + str(matrix[length][length]))
    print("Sequence: " + "".join(sub))

with open(sys.argv[1]) as input1:
    string1 = input1.readline().strip()

lcs(string1, len(string1))
