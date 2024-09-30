class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, node, data):
        # node is the parent node to which the data should be add
        node.children.append(TreeNode(data))

    def setRoot(self, data):
        self.root = TreeNode(data)
