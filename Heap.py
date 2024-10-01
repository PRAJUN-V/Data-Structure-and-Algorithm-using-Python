class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, child_index):
        return (child_index - 1) // 2

    def left_child(self, parent_index):
        return (2 * parent_index) + 1

    def right_child(self, parent_index):
        return (2 * parent_index) + 2

    # Insert element into the heap and heapify up
    def insert(self, data):
        self.heap.append(data)
        curr_index = len(self.heap) - 1
        # Heapify up
        while curr_index != 0:
            parent_index = self.parent(curr_index)
            if self.heap[curr_index] < self.heap[parent_index]:
                self.heap[curr_index], self.heap[parent_index] = self.heap[parent_index], self.heap[curr_index]
                curr_index = parent_index
            else:
                break

    # Delete the root element (minimum element) from the heap
    def delete(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()

        # Swap the root with the last element and remove the last element
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        # Heapify down from the root
        curr_index = 0
        while True:
            left = self.left_child(curr_index)
            right = self.right_child(curr_index)
            smallest = curr_index

            # Find the smallest among current, left child, and right child
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            # If the smallest is not the current node, swap and continue heapifying down
            if smallest != curr_index:
                self.heap[curr_index], self.heap[smallest] = self.heap[smallest], self.heap[curr_index]
                curr_index = smallest
            else:
                break

        return min_value

    def print_heap(self):
        print(self.heap)


# Example usage
h1 = MinHeap()
l = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
for i in l:
    h1.insert(i)
h1.print_heap()  # Should print the heap structure

print("Deleted root:", h1.delete())  # Deletes the minimum element (root)
h1.print_heap()  # Should print the heap after deletion
