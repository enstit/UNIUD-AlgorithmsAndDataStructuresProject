class Node():
    def __init__(self, value, str_name):
        self.key = value
        self.name = str_name
        self.left = None
        self.right = None


def bst_insert(root, value, str_name):
    if root is None:
        return Node(value, str_name)

    if value < root.key:
        root.left = bst_insert(root.left, value, str_name)
    else:
        root.right = bst_insert(root.right, value, str_name)

    return root


def bst_find(root, value):
    if root is None:
        return

    if root.key == value:
        print(root.name)

    if root.key < value:
        return bst_find(root.right, value)

    return bst_find(root.left, value)


def show(root):
    if root:
        print(str(root.key) + ":" + root.name, end=" ")
        if (root.left is None):
            print("NULL", end=" ")
        if (root.right is None):
            print("NULL", end=" ")
        show(root.left)
        show(root.right)


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
