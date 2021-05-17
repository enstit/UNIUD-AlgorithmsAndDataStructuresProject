from avl import *
from bst import *
from rbt import *
import numpy as np
import random
import time as t
import sys


sys.setrecursionlimit(10**6)

def sizeGenerator(first_size, last_size, span):
    sizes = []
    a = first_size
    b = (last_size/first_size)**(float(1.00/(span-1)))
    for i in range(span):
        sizes.append(int(a*(b**i)))
    return sizes

def runBST(n): # int n -> size of the tree
    node = Node(0, "")
    for i in range(1, n):
        key = i
        #if bst_find(node, key) is None: possiamo omettere il controllo, altrimenti dobbiamo usare la versione iterativa
        bst_insert_iterative(node, key, "")

def runAVL(n): # int n -> size of the tree
    node = AVLNode(0, "")
    for i in range(1, n):
        key = i
        #if avl_find(node, key) == None:
        avl_insert(node, key, "")

def runRBT(n): # int n -> size of the tree
    node = RedBlackTree()
    node.rbt_insert(0, "")
    for i in range(1, n):
        key = i
        #if rbt_find(node.root, key) == None:
        node.rbt_insert(key, "")

def timingsBST(dim, t_min):
	timings = []
	for n in dim:
	    i = 0
	    t_passed = 0
	    while ( t_passed <= t_min ):
	        start = t.time()
	        runBST(n)
	        end = t.time()
	        i += 1
	        t_passed += end-start
	    timings.append((t_passed/i)/n)
	return timings

def timingsAVL(dim, t_min):
	timings = []
	for n in dim:
	    i = 0
	    t_passed = 0
	    while ( t_passed <= t_min ):
	        start = t.time()
	        runAVL(n)
	        end = t.time()
	        i += 1
	        t_passed += end-start
	    timings.append((t_passed/i)/n)
	return timings

def timingsRBT(dim, t_min):
	timings = []
	for n in dim:
	    i = 0
	    t_passed = 0
	    while ( t_passed <= t_min ):
	        start = t.time()
	        runRBT(n)
	        end = t.time()
	        i += 1
	        t_passed += end-start
	    timings.append((t_passed/i)/n)
	return timings



def main():

	# Set chosen parameters
	FIRST_SIZE = 1000
	LAST_SIZE = 10000
	RANGE = 100

	# Generate input array
	dim = sizeGenerator(FIRST_SIZE,LAST_SIZE,RANGE)

	# System time resolution
	TIME_ERROR = 0.001

	start = t.time()
	end = t.time()

	while (start == end):
		end = t.time()

	r = end - start
	t_min = r*((1/TIME_ERROR)+1)

	tBST = timingsBST(dim, t_min)
	tAVL = timingsAVL(dim, t_min)
	tRBT = timingsRBT(dim, t_min)

	stdBST = np.std(tBST)
	stdAVL = np.std(tAVL)
	stdRBT = np.std(tRBT)

	#for i in range(RANGE):
	#	print(dim[i], tBST[i], np.std(tBST), tAVL[i], np.std(tAVL), tRBT[i], np.std(tRBT), sep=',')

	for i in range(RANGE):
		print str(dim[i]) + ',' + str(tBST[i]) + ',' + str(stdBST) + ',' + str(tAVL[i]) + ',' + str(stdAVL) + ',' + str(tRBT[i]) + ',' + str(stdRBT)

if __name__ == '__main__':
	main()
























