from avl import *
from bst import *
from rbt import *
import random
import time as t


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
        if bst_find(node, key) is None:
            bst_insert(node, key, "")

def runAVL(n): # int n -> size of the tree
    node = AVLNode(0, "")
    for i in range(1, n):
        key = i
        if avl_find(node, key) is None:
            avl_insert(node, key, "")

def runRBT(n): # int n -> size of the tree
    node = RedBlackTree()
    node.rbt_insert(0, "")
    for i in range(1, n):
        key = i
        if rbt_find(node.root, key) is None:
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


def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    return sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def stddev(data, ddof=0):
    """Calculates the population standard deviation
    by default; specify ddof=1 to compute the sample
    standard deviation."""
    n = len(data)
    ss = _ss(data)
    pvar = ss/(n-ddof)
    return pvar**0.5



def main():

        # Set chosen parameters
        FIRST_SIZE = 1000
        LAST_SIZE = 5000
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

        stdBST = stddev(tBST)
        stdAVL = stddev(tAVL)
        stdRBT = stddev(tRBT)


        for i in range(RANGE):
            print str(dim[i]), str(tBST[i]), str(stdBST), str(tAVL[i]), str(stdAVL), str(tRBT[i]), str(stdRBT)

if __name__ == '__main__':
        main()
