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

    def pop(self, index=0):
        if index >= self.length:
            raise IndexError('pop index out of range')

        elif index == 0:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp.data

        else:
            currentNode = self.head
            for _ in range(index - 1):
                currentNode = currentNode.next
            temp = currentNode.next.data
            currentNode.next = currentNode.next.next
            self.length -= 1
            return temp

    def __delitem__(self, index):
        self.pop(index)

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)

        elif index == self.length :
            self.append(data)

        elif index > self.length - 1 or index < 0:
            raise IndexError('Invalid index')

        else:
            new_node = Node(data)
            currentNode = self.head
            for _ in range(index - 1):
                currentNode = currentNode.next
            new_node.next = currentNode.next
            currentNode.next = new_node
            self.length += 1



if __name__ == "__main__":
    ll = LinkedList()
    for i in range(10):
        ll.append(i)

    print(ll)
    ll.insert(7, 1983)
    ll.insert(0, 235)
    ll.insert(12, 897897)
    print(ll)

