from CustomHashFunction import my_own_hash_function
from LinkedList import LinkedList


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

    def find(self, key):
        hashValue = my_own_hash_function(key)
        index = hashValue % self.size
        currentNode = self.hashTable[index].head
        while currentNode is not None:
            if currentNode.data[0] == key:
                return currentNode.data[1]
            currentNode = currentNode.next
        raise KeyError(f'Key {key} not found')

    def __getitem__(self, key):
        try:
            return self.find(key)
        except KeyError:
            raise KeyError(f'Key {key} not found')


if __name__ == '__main__':
    ht = HashTable()
    ht.add(0, 'hello world')
    ht.add(1, 'aeroplane')
    ht.add('h', 'hello')
    print(ht.hashTable[1])
    print(ht.find(1))
    print(ht.find('h'))
    print(ht[2])
