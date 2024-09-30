class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, child_index):
        return (child_index - 1) // 2

    def left_child(self, parent_index):
        return (2 * parent_index) + 1

    def right_child(self, parent_index):
        return (2 * parent_index) + 2

    # In heap insertion is from leaf and deletion is from root.
    def insert(self, data):
        self.heap.append(data)
        # Now I need to heapify up to bring the inserted value in its real place
        curr_index = len(self.heap) - 1
        while curr_index != 0:
            parent_index = self.parent(curr_index)
            if self.heap[curr_index] < self.heap[parent_index]:
                self.heap[curr_index], self.heap[parent_index] = self.heap[parent_index], self.heap[curr_index]
                curr_index = parent_index
            else:
                break

    def print_heap(self):
        print(self.heap)


h1 = MinHeap()
# print(h1.parent(6))
# print(h1.left_child(1))
# print(h1.right_child(1))
h1.insert(8)
h1.insert(1)
h1.insert(9)
h1.insert(0)
h1.insert(2)
h1.insert(3)
h1.print_heap()
