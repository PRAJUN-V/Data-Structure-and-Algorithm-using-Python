from CustomHashFunction import my_own_hash_function
from LinkedList import LinkedList
import sys

class HashTable:
    def __init__(self):
        # Initially I have set the size of hash table as 10
        self.size = 10
        self.hashTable = [LinkedList() for _ in range(self.size)]

    def add(self, key, value):
        hashValue = my_own_hash_function(key)

        index = hashValue % self.size

        self.hashTable[index].append([key, value])


    def __str__(self):
        return str(self.hashTable)

if __name__ == '__main__':
    ht = HashTable()
    ht.add('hello world is the key', 'value')
    ht.add(2, 'hi')
    ht.add(1, 'papa')
    ht.add(True, 'hello')
    print(ht.hashTable[1])
    print(ht.hashTable[2])
    print(ht)
    print(sys.getsizeof(ht))
