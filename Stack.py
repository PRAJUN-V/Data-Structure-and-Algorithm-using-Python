from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.linkedlist = LinkedList()

    def push(self, data):
        self.linkedlist.prepend(data)

    def __str__(self):
        return self.linkedlist.__str__()

    def pop(self):
        if self.linkedlist.head is None:
            raise IndexError("Pop from empty stack")
        value = self.linkedlist.head.data
        self.linkedlist.head = self.linkedlist.head.next
        return value


if __name__ == "__main__":
    s = Stack()
    s.push(34)
    s.push(56)
    s.push(67)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s)

