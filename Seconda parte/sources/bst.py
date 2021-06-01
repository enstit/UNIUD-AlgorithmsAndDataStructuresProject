from Node import Node

"""
insert a key value in a tree
:param root: BSTNode object that represents
    the root of the tree
:param value: an integer representing the value to insert
:param str_name: a string corresponding to
    the literal format of the value
:return: a BSTNode object
"""


def bst_insert(root, key, str_name):
 
    curr = root
 
    parent = None
 
    if root is None:
        return Node(key, str_name)
 
    while curr:
 
        parent = curr
 
        if key < curr.key:
            curr = curr.left
        else:
            curr = curr.right
 
    if key < parent.key:
        parent.left = Node(key, str_name)
    else:
        parent.right = Node(key, str_name)
 
    return root


def bst_insert_recursive(root, value, str_name):
    if root is None:
        return Node(value, str_name)
    if value < root.key:
        root.left = bst_insert(root.left, value, str_name)
    else:
        root.right = bst_insert(root.right, value, str_name)
    return root


"""
print the found value in a literal format
:param root: BSTNode object that represents
    the root of the tree
:param value: an integer representing the value to find
"""


def bst_find(root, value):
    x = root
    while x is not None:
        if x.key == value:
            return x.name
        if x.key < value:
            x = x.right
        else:
            x = x.left
    return


def bst_find_recursive(root, value):
    if root is None:
        return
    if root.key == value:
        return root.name
    if root.key < value:
        return bst_find(root.right, value)
    return bst_find(root.left, value)


    """
    print the tree in a preorder visit
    :param root: BSTNode object that represents
        the root of the tree
    """
def bst_show(root):
    if root:
        print(
            str(root.key), root.name,
            sep=":",
            end=" "
            )
        bst_show(root.left)
        bst_show(root.right)
    else:
        print("NULL", end=" ")

# def bst_show_python2(root):
#     """
#     print the tree in a preorder visit
#     :param root: BSTNode object that represent the root of the tree
#     """
#     if root:
#         print str(root.key) + ":" + root.name
#         show(root.left)
#         show(root.right)
#     else:
#         print "NULL"


def inorder_visit(root):
    if root:
        inorder_visit(root.left)
        print(root.name)
        inorder_visit(root.right)


def preorder_visit(root):
    if root:
        print(root.name)
        preorder_visit(root.left)
        preorder_visit(root.right)


def postorder_visit(root):
    if root:
        postorder_visit(root.left)
        postorder_visit(root.right)
        print(root.name)