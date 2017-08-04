import sys

# Creates dictionary of Date to Data from input A
data_a = {}
with open(sys.argv[1]) as input1:
    num_a = input1.readline()
    for line in input1:
        str1 = line.strip()
        if str1 == "":
            break
        str_a = str1.split(" ")
        data_a[str_a[0]] = str_a[1]

# Creates dictionary of Date to Data from input B
data_b = {}
with open(sys.argv[2]) as input2:
    num_b = input2.readline()
    for line in input2:
        str1 = line.strip()
        if str1 == "":
            break
        str_b = str1.split(" ")
        data_b[str_b[0]] = str_b[1]

# Loops through data from A and compares it against data in B
for key in data_a:
    if key in data_b:
        # If the Date from A matches date in B but data doesn't match
        if data_a[key] != data_b[key]:
            print("Inconsistent Data (" + key + "): A: " +
                  data_a[key] + " B: " + data_b[key])
        # Clears out B data if match has already been completed
        del data_b[key]
    # If their is no match in B for the Date in A
    else:
        print("Missing Data (" + key + ") in data set A but not in B")

# The remaining entries in B are entries where their is no matching date in A
for key in data_b:
    print("Missing Data (" + key + ") in data set B but not in A")
