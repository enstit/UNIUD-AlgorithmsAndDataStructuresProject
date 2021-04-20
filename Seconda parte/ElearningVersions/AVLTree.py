class AVLNode():
    def __init__(self, value, str_name):
        self.key = value
        self.name = str_name
        self.left = None
        self.right = None
        self.height = 1


def avl_insert(root, value, str_name):
    """
    insert a key value in a tree
    :param root: AVLNode object that represent the root of the tree
    :param value: an integer representing the value to insert
    :param str_name: a string corresponding to the literal format of the value
    :return: an AVLNode object
    """
    if root is None:
        return AVLNode(value, str_name)

    if value < root.key:
        root.left = avl_insert(root.left, value, str_name)
    else:
        root.right = avl_insert(root.right, value, str_name)

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

    balance = getBalance(root)

    # LL
    if balance > 1 and value < root.left.key:
        return rightRotate(root)

    # RR
    if balance < -1 and value > root.right.key:
        return leftRotate(root)

    # LR
    if balance > 1 and value > root.left.key:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # RL
    if balance < -1 and value < root.right.key:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root


def avl_show(root):
    """
    print the tree in a preorder visit
    :param root: AVLNode object that represent the root of the tree
    """
    if root:
        print str(root.key) + ":" + root.name + ":" + str(root.height), 
        avl_show(root.left)
        avl_show(root.right)
    else:
        print "NULL",


def avl_find(root, value):
    """
    print the found value in a literal format
    :param root: AVLNode object that represent the root of the tree
    :param value: an integer representing the value to find
    """
    if root is None:
        return

    if root.key == value:
        print(root.name)

    if root.key < value:
        return avl_find(root.right, value)

    return avl_find(root.left, value)


#####################################################


def getHeight(root):
    if root is None:
        return 0
    else:
        return root.height


def getBalance(root):
    if root is None:
        return 0
    else:
        return getHeight(root.left) - getHeight(root.right)


def rightRotate(z):
    y = z.left
    T = y.right

    y.right = z
    z.left = T

    z.height = 1 + max(getHeight(z.left), getHeight(z.right))

    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y


def leftRotate(z):
    y = z.right
    T = y.left

    y.left = z
    z.right = T

    z.height = 1 + max(getHeight(z.left), getHeight(z.right))

    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y

        
###########################################
t = None

in_value = raw_input()
in_value = in_value.split(" ")

while(in_value[0] != "exit"):

    if(in_value[0] == "insert"):
        t = avl_insert(t, int(in_value[1]), in_value[2])

    if(in_value[0] == "find"):
        t = avl_find(t, int(in_value[1]))

    if(in_value[0] == "show"):
        avl_show(t)
        print

    in_value = raw_input()
    in_value = in_value.split(" ")