class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            while True:
                if currentNode.next is not None:
                    currentNode = currentNode.next
                else:
                    currentNode.next = node
                    break
        self.length += 1

    def prepend(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def __str__(self):
        if self.head is None:
            return "Linked List is empty"
        else:
            nodes = []
            currentNode = self.head
            while currentNode is not None:
                nodes.append(str(currentNode.data))
                currentNode = currentNode.next
            return ' -> '.join(nodes) + ' -> None'

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        currentNode = self.head
        for _ in range(index):
            currentNode = currentNode.next
        return currentNode.data

    def __setitem__(self, index, data):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        currentNode = self.head
        for _ in range(index):
            currentNode = currentNode.next
        currentNode.data = data

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(10):
        ll.append(i)
    ll[9] = 100
    print(ll)
