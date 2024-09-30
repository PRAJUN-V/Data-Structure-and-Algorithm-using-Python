class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
        else:
            curr_node = self.root
            while True:
                if data < curr_node.data:
                    if curr_node.left is None:
                        curr_node.left = BSTNode(data)
                        break
                    else:
                        curr_node = curr_node.left

                elif data > curr_node.data:
                    if curr_node.right is None:
                        curr_node.right = BSTNode(data)
                        break
                    else:
                        curr_node = curr_node.right

                else:
                    # If data already exists in the tree, do nothing (no duplicates)
                    break
