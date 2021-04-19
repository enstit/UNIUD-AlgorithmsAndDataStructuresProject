from bst import *
"""
INPUT OPERATION:
    - insert 'key value' 'literal key value'
    - find 'key value'
    - show 
    - exit

Example of use:
in:     insert 1 one
in:     insert 3 three
in:     insert 2 two
in:     show
out:    1:one NULL 3:three NULL 2:two NULL NULL
in:     find 2 
out:    two
in:     exit
"""
TREE_TYPE = "BST"  # "AVL" | "RBT"
t = None

in_value = input()
in_value = in_value.split(" ")

while(in_value[0] != "exit"):

    if(in_value[0] == "insert"):
        if(TREE_TYPE == "BST"):
            t = bst_insert(t, int(in_value[1]), in_value[2])

    if(in_value[0] == "find"):
        if (TREE_TYPE == "BST"):
            bst_find(t, int(in_value[1]))

    if(in_value[0] == "show"):
        if (TREE_TYPE == "BST"):
            bst_show(t)
            print()

    in_value = input()
    in_value = in_value.split(" ")
