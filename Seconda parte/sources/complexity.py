from avl import *
from bst import *
from rbt import *
import csv
import matplotlib.pyplot as plt
import random
import statistics as st
import time as t


# Create an array with exponential sizes
# in range(FIRST_SIZE,LAST_SIZE)
def sizeGenerator(first_size, last_size, span):
    sizes = []
    a = first_size
    b = (last_size/first_size)**(float(1/(span-1)))
    for i in range(span):
        sizes.append(int(a*(b**i)))
    return sizes

# Generate a keys list, of lenght n
def generateKeys(n):
    a = []
    for i in range(n):
        a.append(random.randint(0, MAX_KEY))
    return a

# Generate list of lists to be used with runAVL/BST/RBTsmart()
def generateInput(dim):
    a = []
    for i in dim:
        a.append(generateKeys(i))
    return a

# Set chosen parameters
FIRST_SIZE = 1_000
LAST_SIZE = 100_000
RANGE = 100
MAX_KEY = 2147483647

##############################

# Generate input array
dim = sizeGenerator(FIRST_SIZE,LAST_SIZE,RANGE)

def runBSTrandom(n): # int n -> size of the tree
    node = Node(random.randint(0, MAX_KEY), "")
    for i in range(0, n):
        key = random.randint(0, MAX_KEY)
        if bst_find(node, key) == None:
            bst_insert(node, key, "")

def runAVLrandom(n): # int n -> size of the tree
    node = AVLNode(random.randint(0, MAX_KEY), "")
    for i in range(0, n):
        key = random.randint(0, MAX_KEY)
        if avl_find(node, key) == None:
            avl_insert(node, key, "")

def runRBTrandom(n): # int n -> size of the tree
    node = RedBlackTree()
    node.rbt_insert(random.randint(0, MAX_KEY), "")
    for i in range(0, n):
        key = random.randint(0, MAX_KEY)
        if rbt_find(node.root, key) == None:
            node.rbt_insert(key, "")

##############################

def runBSTsorted(n): # int n -> size of the tree
    node = Node(0, "")
    for i in range(1, n):
        key = i
        bst_insert_iterative(node, key, "")

def runAVLsorted(n): # int n -> size of the tree
    node = AVLNode(0, "")
    for i in range(1, n):
        key = i
        avl_insert(node, key, "")

def runRBTsorted(n): # int n -> size of the tree
    node = RedBlackTree()
    node.rbt_insert(0, "")
    for i in range(1, n):
        key = i
        #if rbt_find(node.root, key) == None:
        node.rbt_insert(key, "")

##############################

# def runBSTsmart(n): # n -> list of keys to generate bst
#     node = Node(random.randint(0, MAX_KEY), "")
#     for i in n:
#         key = i
#         if bst_find(node, key) == None:
#             bst_insert(node, key, "")

# def runAVLsmart(n): # n -> list of keys to generate avl tree
#     node = AVLNode(random.randint(0, MAX_KEY), "")
#     for i in n:
#         key = i
#         if avl_find(node, key) == None:
#             avl_insert(node, key, "")

# def runRBTsmart(n): # n -> list of keys to generate rbt
#     node = RedBlackTree()
#     node.rbt_insert(random.randint(0, MAX_KEY), "")
#     for i in n:
#         key = i
#         if rbt_find(node.root, key) == None:
#             node.rbt_insert(key, "")

##############################

# System time resolution

TIME_ERROR = 0.001

start = t.time()
end = t.time()

while (start == end):
    end = t.time()

r = end - start
t_min = r*((1/TIME_ERROR)+1)

#print(t_min)

##############################

#############################
####### RANDOM METHOD #######
#############################

# Create an array with averege amortized timings for BST
amortizedTimes_BST = []
for n in dim:
    i = 0
    t_passed = 0
    while ( t_passed <= t_min ):
        start = t.time()
        runBSTrandom(n)
        end = t.time()
        i += 1
        t_passed += end-start
    amortizedTimes_BST.append((t_passed/i)/n) 

# Create an array with averege amortized timings for AVL
amortizedTimes_AVL = []
for n in dim:
    i = 0
    t_passed = 0
    while ( t_passed <= t_min ):
        start = t.time()
        runAVLrandom(n)
        end = t.time()
        i += 1
        t_passed += end-start
    amortizedTimes_AVL.append((t_passed/i)/n)

# Create an array with averege amortized timings for RBT
amortizedTimes_RBT = []
for n in dim:
    i = 0
    t_passed = 0
    while ( t_passed <= t_min ):
        start = t.time()
        runRBTrandom(n)
        end = t.time()
        i += 1
        t_passed += end-start
    amortizedTimes_RBT.append((t_passed/i)/n)

row_list = [['id', 'size', 'amortizedTimes_BST', 'deviazioneStandard_BST', 'amortizedTimes_AVL', 'deviazioneStandard_AVL', 'amortizedTimes_RBT', 'deviazioneStandard_RBT']]
for i in range(RANGE):
    row_list.append([
        i, dim[i], amortizedTimes_BST[i], st.stdev(amortizedTimes_BST),
        amortizedTimes_AVL[i], st.stdev(amortizedTimes_AVL), 
        amortizedTimes_RBT[i], st.stdev(amortizedTimes_RBT)
     ])

with open('results-random.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

##############################

#############################
####### SORTED METHOD #######
#############################

# Create an array with averege amortized timings for RBT
amortizedTimes_BST_sorted = []
for n in dim:
    i = 0
    t_passed = 0
    while ( t_passed <= t_min ):
        start = t.time()
        runBSTsorted(n)
        end = t.time()
        i += 1
        t_passed += end-start
    amortizedTimes_BST_sorted.append((t_passed/i)/n)

# Create an array with averege amortized timings for RBT
amortizedTimes_AVL_sorted = []
for n in dim:
    i = 0
    t_passed = 0
    while ( t_passed <= t_min ):
        start = t.time()
        runAVLsorted(n)
        end = t.time()
        i += 1
        t_passed += end-start
    amortizedTimes_AVL_sorted.append((t_passed/i)/n)

# Create an array with averege amortized timings for RBT
amortizedTimes_RBT_sorted = []
for n in dim:
    i = 0
    t_passed = 0
    while ( t_passed <= t_min ):
        start = t.time()
        runRBTsorted(n)
        end = t.time()
        i += 1
        t_passed += end-start
    amortizedTimes_RBT_sorted.append((t_passed/i)/n)

row_list = [['id', 'size', 'amortizedTimes_BST', 'deviazioneStandard_BST', 'amortizedTimes_AVL', 'deviazioneStandard_AVL', 'amortizedTimes_RBT', 'deviazioneStandard_RBT']]
for i in range(RANGE):
    row_list.append([
        i, dim[i], amortizedTimes_BST_sorted[i], st.stdev(amortizedTimes_BST_sorted),
        amortizedTimes_AVL_sorted[i], st.stdev(amortizedTimes_AVL_sorted),
        amortizedTimes_RBT_sorted[i], st.stdev(amortizedTimes_RBT_sorted)
     ])

with open('results-sorted.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)