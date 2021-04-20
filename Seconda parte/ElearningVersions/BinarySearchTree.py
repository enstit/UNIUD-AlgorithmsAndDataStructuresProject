class Node():
    def __init__(self, value, str_name):
        self.key = value
        self.name = str_name
        self.left = None
        self.right = None


def bst_insert(root, value, str_name):
    """
    insert a key value in a tree
    :param root: BSTNode object that represent the root of the tree
    :param value: an integer representing the value to insert
    :param str_name: a string corresponding to the literal format of the value
    :return: a BSTNode object
    """
    if root is None:
        return Node(value, str_name)

    if value < root.key:
        root.left = bst_insert(root.left, value, str_name)
    else:
        root.right = bst_insert(root.right, value, str_name)

    return root


def bst_find(root, value):
    """
    print the found value in a literal format
    :param root: BSTNode object that represent the root of the tree
    :param value: an integer representing the value to find
    """
    if root is None:
        return

    if root.key == value:
        print(root.name)
        return

    if root.key < value:
        return bst_find(root.right, value)

    return bst_find(root.left, value)


def show(root):
    """
    print the tree in a preorder visit
    :param root: BSTNode object that represent the root of the tree
    """
    if root:
        print str(root.key) + ":" + root.name, 
        show(root.left)
        show(root.right)
    else:
        print "NULL",
        
###########################################
t = None

in_value = raw_input()
in_value = in_value.split(" ")

while(in_value[0] != "exit"):

    if(in_value[0] == "insert"):
        t = bst_insert(t, int(in_value[1]), in_value[2])

    if(in_value[0] == "find"):
        t = bst_find(t, int(in_value[1]))

    if(in_value[0] == "show"):
        show(t)
        print

    in_value = raw_input()
    in_value = in_value.split(" ")