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


# Testing

test_values = [[1, 2, 3, 4, 5],
               [5, 4, 3, 2, 1],
               [1, -1, 0, 9, 8, -9],
               [1, 1, 1, 2, 2, 3, 3, 3],
               [-5, -3, -1, -4, -2]]

p1 = PriorityQueue()
p2 = PriorityQueue()
p3 = PriorityQueue()
p4 = PriorityQueue()
p5 = PriorityQueue()

for i in test_values[0]:
    p1.append(i)

for i in test_values[1]:
    p2.append(i)

for i in test_values[2]:
    p3.append(i)

for i in test_values[3]:
    p4.append(i)

for i in test_values[4]:
    p5.append(i)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
