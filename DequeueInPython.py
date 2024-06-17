from collections import deque
# deque can be used as both stack and queue. Full form of dequeue is double ended queue.

dd = deque()
dd.append(1)
dd.appendleft(2)
dd.extendleft([5, 6, 7, 8])
dd.extend([11, 22, 33, 44])
print(dd)
dd.clear()
print(dd)
