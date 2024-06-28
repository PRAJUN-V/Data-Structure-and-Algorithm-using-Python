class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            prevNode = None
            while currentNode is not None:
                if data <= currentNode.data:
                    if currentNode == self.head:
                        node.next = self.head
                        self.head = node
                    else:
                        node.next = currentNode
                        prevNode.next = node
                    break
                prevNode = currentNode
                currentNode = currentNode.next
            if currentNode is None:
                prevNode.next = node

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

    # For converting priority queue or linked list to list we need to make it iterable object by
    # defining a __iter__ method in it.
    def __iter__(self):
        currentNode = self.head
        while currentNode is not None:
            yield currentNode.data
            currentNode = currentNode.next


# Testing

test_values = [[1, 2, 3, 4, 5],
               [5, 4, 3, 2, 1],
               [1, -1, 0, 9, 8, -9],
               [1, 1, 1, 2, 2, 3, 3, 3],
               [-5, -3, -1, -4, -2],
               [0, 2, 5, -9, 9, 100, -3]]

for i in test_values:
    p1 = PriorityQueue()
    for j in i:
        p1.append(j)
    print(p1)
    print(list(p1))
