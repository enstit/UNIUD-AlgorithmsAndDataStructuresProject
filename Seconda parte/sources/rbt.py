from Node import RBTNode


class RedBlackTree():
    def __init__(self):
        self.TNIL = RBTNode(None, None)
        self.TNIL.color = "black"
        self.TNIL.left = None
        self.TNIL.right = None
        self.root = self.TNIL


    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.TNIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.TNIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


    def rbt_insert(self, value, str_name):
        z = RBTNode(value, str_name)
        z.left = self.TNIL
        z.right = self.TNIL
        y = self.TNIL
        x = self.root
        while x != self.TNIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.TNIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self.insert_fix_up(z)


    def insert_fix_up(self, z):
        while z.parent.color == "red":
            if z.parent == z.parent.parent.right:
                y = z.parent.parent.left
                if y.color == "red":
                    y.color = "black"
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)
            else:
                y = z.parent.parent.right
                if y.color == "red":
                    y.color = "black"
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent)
            if z == self.root:
                break
        self.root.color = "black"


"""
print the tree in a preorder visit
:param root: RBTNode object that represents
    the root of the tree (accessed by t.root in the calling)
"""
def rbt_show(root):
    if root.key is None:
        print("NULL", end=" ")
        return
    if root.name is None:
        print("NULL", end=" ")
        return
    if root:
        print(
            str(root.key), root.name, str(root.color),
            sep=":",
            end=" "
            )       
        rbt_show(root.left)
        rbt_show(root.right)
    else:
        print("NULL", end=" ")


# def rbt_show_python2(root):
#     if root.key is None:
#         print "NULL",
#         return
#     if root.name is None:
#         print "NULL", 
#         return
#     if root:
#         print str(root.key) + ":" + root.name + ":" + str(root.color) 
#         rbt_show(root.left)
#         rbt_show(root.right)
#     else:
#         print "NULL"

"""
reutrn the found value in a literal format
:param root: RBTNode object that represents
    the root of the tree (accessed by t.root in the calling)
:param value: an integer representing the value to find
"""

def rbt_find(root, value):
    curr = root

    while (curr is not None) and (curr.key is not None) and (curr.name is not None):
        if curr.key == value:
            return curr.name
        if curr.key < value:
            curr = curr.right
        else:
            curr = curr.left
    return


def rbt_find_recursive(root, value):
    if root.key is None:
        return
    if root.name is None:
        return
    if root is None:
        return
    if root.key == value:
        return root.name
    if root.key < value:
        return rbt_find(root.right, value)
    return rbt_find(root.left, value)
