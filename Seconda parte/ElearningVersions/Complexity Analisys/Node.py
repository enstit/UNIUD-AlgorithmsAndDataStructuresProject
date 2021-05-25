class Node(object):
    def __init__(self, value, str_name):
        self.key = value
        self.name = str_name
        self.left = None
        self.right = None


class AVLNode(Node):
    def __init__(self, value, str_name):
        super(AVLNode,self).__init__(value, str_name)
        self.height = 1


class RBTNode(Node):
    def __init__(self, value, str_name):
        super(RBTNode,self).__init__(value, str_name)
        self.parent = None
        self.color = "red"