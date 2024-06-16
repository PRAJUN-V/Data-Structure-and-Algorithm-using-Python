from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def enqueue(self, data):
        self.linkedlist.append(data)

    def __str__(self):
        return self.linkedlist.__str__()

    def dequeue(self):
        if self.linkedlist.head is None:
            raise IndexError("Dequeue from empty queue")
        value = self.linkedlist.head.data
        self.linkedlist.head = self.linkedlist.head.next
        return value

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    try:
        print(q.dequeue())
        print(q.dequeue())
    except IndexError as e:
        print('Error is ', e)

