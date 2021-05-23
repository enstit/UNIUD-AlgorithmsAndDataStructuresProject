from avl import *
from bst import *
from rbt import *
import numpy as np
import random
import time as t


def sizeGenerator(first_size, last_size, span):
    sizes = []
    a = first_size
    b = (last_size/first_size)**(float(1.00/(span-1)))
    for i in range(span):
        sizes.append(int(a*(b**i)))
    return sizes

# Generate a keys list, of lenght n
def _generateKeys(n, MAX_KEY):
    a = []
    for i in range(n):
        a.append(random.randint(0, MAX_KEY))
    return a

# Generate list of lists to be used with runAVL/BST/RBTsmart()
def generateInput(dim, MAX_KEY):
    a = []
    for i in dim:
        a.append(_generateKeys(i, MAX_KEY))
    return a

def runBST(n, MAX_KEY): # n -> list of keys to generate bst
    node = Node(random.randint(0, MAX_KEY), "")
    for i in n:
        key = i
        if bst_find(node, key) == None:
            bst_insert(node, key, "")

def runAVL(n, MAX_KEY): # n -> list of keys to generate avl tree
    node = AVLNode(random.randint(0, MAX_KEY), "")
    for i in n:
        key = i
        if avl_find(node, key) == None:
            avl_insert(node, key, "")

def runRBT(n, MAX_KEY): # n -> list of keys to generate rbt
    node = RedBlackTree()
    node.rbt_insert(random.randint(0, MAX_KEY), "")
    for i in n:
        key = i
        if rbt_find(node.root, key) == None:
            node.rbt_insert(key, "")

def timingsBST(generated_nodes, t_min, MAX_KEY):
	timings = []
	for n in generated_nodes:
	    i = 0
	    t_passed = 0
	    while ( t_passed <= t_min ):
	        start = t.time()
	        runBST(n, MAX_KEY)
	        end = t.time()
	        i += 1
	        t_passed += end-start
	    timings.append((t_passed/i)/len(n))
	return timings

def timingsAVL(generated_nodes, t_min, MAX_KEY):
	timings = []
	for n in generated_nodes:
	    i = 0
	    t_passed = 0
	    while ( t_passed <= t_min ):
	        start = t.time()
	        runAVL(n, MAX_KEY)
	        end = t.time()
	        i += 1
	        t_passed += end-start
	    timings.append((t_passed/i)/len(n))
	return timings

def timingsRBT(generated_nodes, t_min, MAX_KEY):
	timings = []
	for n in generated_nodes:
	    i = 0
	    t_passed = 0
	    while ( t_passed <= t_min ):
	        start = t.time()
	        runRBT(n, MAX_KEY)
	        end = t.time()
	        i += 1
	        t_passed += end-start
	    timings.append((t_passed/i)/len(n))
	return timings



def main():

	# Set chosen parameters
	FIRST_SIZE = 1000
	LAST_SIZE = 10000
	RANGE = 100
	MAX_KEY = 2147483647

	# Generate input array
	dim = sizeGenerator(FIRST_SIZE,LAST_SIZE,RANGE)
	generated_nodes = generateInput(dim, MAX_KEY)

	# System time resolution
	TIME_ERROR = 0.001

	start = t.time()
	end = t.time()

	while (start == end):
		end = t.time()

	r = end - start
	t_min = r*((1/TIME_ERROR)+1)


	tBST = timingsBST(generated_nodes, t_min, MAX_KEY)
	tAVL = timingsAVL(generated_nodes, t_min, MAX_KEY)
	tRBT = timingsRBT(generated_nodes, t_min, MAX_KEY)

	stdBST = np.std(tBST)
	stdAVL = np.std(tAVL)
	stdRBT = np.std(tRBT)

	#for i in range(RANGE):
	#	print(dim[i], tBST[i], np.std(tBST), tAVL[i], np.std(tAVL), tRBT[i], np.std(tRBT), sep=',')

	for i in range(RANGE):
		print str(dim[i]), str(tBST[i]), str(stdBST), str(tAVL[i]), str(stdAVL), str(tRBT[i]), str(stdRBT)

if __name__ == '__main__':
	main()
