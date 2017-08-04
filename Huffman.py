import heapq
import sys
from operator import itemgetter


# Small node class to build huffman tree with
class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data
        self.weight = None

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def getData(self):
        return self.data

    # this comparator is for the heap
    def __lt__(self, other):
        return self.weight < other.weight

chars = {}
count = 0
# read input file and process occurrences of each character to dictionary
with open(sys.argv[1]) as input1:
    for line in input1:
        for char in line:
            count += 1
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

for char1 in chars:
    chars[char1] = (chars[char1] / float(count)) * 100

h = []
# creates nodes and and adds them to heap
for key in chars:
    node = Node(key)
    node.setWeight(chars[key])
    heapq.heappush(h, node)

# builds the huffman tree using heap
while len(h) > 1:
    node = Node()
    node_a = heapq.heappop(h)
    node_b = heapq.heappop(h)
    node.left = node_a
    node.right = node_b
    freq = node_a.getWeight() + node_b.getWeight()
    node.setWeight(freq)
    heapq.heappush(h, node)

# root node for huffman tree
node = heapq.heappop(h)


# traverses tree and builds codeword path
def decoding(n, path, list2):
    if n.left is not None:
        decoding(n.left, path + "0", list2)
    if n.right is not None:
        decoding(n.right, path + "1", list2)
    if n.left is None and n.right is None:
        list2.append([n.getData(), n.getWeight(), path])
        return list2

list1 = []
list1.append(decoding(node, "", list1))

del list1[len(list1) - 1]
# sort by character
list1.sort(key=itemgetter(0))

print("{:20}{:12}{:12}".format("Character", "Codeword", "Frequency"))

code_len = 0
for item in list1:
    code_len += (len(item[2]) * (item[1] / 100.0))

    if item[0] == "\n":
        print(("{:>9}{:>19}{:12}%".format(" ", item[2], round(item[1], 4))))
    else:
        print(("{:>9}{:>19}{:12}%".format(item[0], item[2], round(item[1], 4))))


original = count * 8
encode = count * code_len
comp = (original - encode) / float(original) * 100
print("{:26}{} bits".format("Average Codeword Length:", round(code_len, 4)))
print("{:26}{}".format("Original (bits):", original))
print("{:26}{}".format("Encoding Size (bits):", round(encode, 4)))
print("{:26}{}%".format("Compression Ratio:", 100 - round(comp, 4)))
