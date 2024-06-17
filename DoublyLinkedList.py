class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.prev = None
        else:
            currentNode = self.head
            while True:
                if currentNode.next is not None:
                    currentNode = currentNode.next
                else:
                    currentNode.next = node
                    currentNode.next.prev = currentNode
                    break
        self.length += 1
