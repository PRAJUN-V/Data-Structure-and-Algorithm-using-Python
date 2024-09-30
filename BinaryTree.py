class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.root = None

bt = BT()
bt.root = BTNode('A')
bt.root.left = BTNode('B')
bt.root.right = BTNode('C')
