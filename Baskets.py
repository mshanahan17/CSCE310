import sys


# Creates powerset of the list of items
def power(set1):
    result = [[]]
    for elem in set1:
        result.extend([x + [elem] for x in result])
    return result


# reads input file and creates a list of all items and a list of baskets
with open(sys.argv[1]) as input1:
    numBaskets = int(input1.readline().strip())
    basketList = []
    baskets = []
    item_list = []
    for line in range(0, numBaskets):
        basket_str = line.strip()
        if basket_str != "":
            bask_list = basket_str.split(",")
            for index, item in enumerate(bask_list):
                bask_list[index] = item.strip()
                if bask_list[index] not in item_list:
                    item_list.append(bask_list[index])
        baskets.append(bask_list)

power_set = power(item_list)

# clears out the empty set of the powerset
del power_set[0]

# sorts the powerset by size of subsets
power_set.sort(key=len)

print("Items: [%s]" % (', '.join(item_list)))
print("Number of baskets: " + str(numBaskets))

# checks if each item from the powerset is a subset of a basket and keeps track of each time
for combo in power_set:
    count = 0
    for basket in baskets:
        if set(combo).issubset(basket):
            count += 1
    if count > 0:
        print(str(count) + " => " + "[%s]" % (', '.join(combo)))
