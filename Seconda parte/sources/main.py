from bst import *

t = None

in_value = input()
in_value = in_value.split(" ")

while(in_value[0] != "exit"):

    if(in_value[0] == "insert"):
        t = bst_insert(t, int(in_value[1]), in_value[2])

    if(in_value[0] == "find"):
        bst_find(t, int(in_value[1]))

    if(in_value[0] == "show"):
        show(t)
        print()

    in_value = input()
    in_value = in_value.split(" ")