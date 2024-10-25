class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode('*')

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode(letter)
            curr_node = curr_node.children[letter]
        curr_node.is_end_of_word = True

    def search(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.is_end_of_word

    def starts_with(self, prefix):
        curr_node = self.root
        for letter in prefix:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return True

    def _collect_words(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)
        for child_letter, child_node in node.children.items():
            self._collect_words(child_node, prefix + child_letter, words)

    def get_words_with_prefix(self, prefix):
        curr_node = self.root
        for letter in prefix:
            if letter not in curr_node.children:
                return []  # Return empty list if prefix is not found
            curr_node = curr_node.children[letter]

        words = []
        self._collect_words(curr_node, prefix, words)
        return words

# Example usage
trie = Trie()
trie.add_word("apple")
trie.add_word("app")
trie.add_word("apply")
trie.add_word("bat")
trie.add_word("ball")
trie.add_word("battle")

# Search for words with the prefix "app"
print(trie.get_words_with_prefix("app"))  # Output: ['app', 'apple', 'apply']

# Search for words with the prefix "ba"
print(trie.get_words_with_prefix("ba"))   # Output: ['bat', 'ball', 'battle']

# Search for words with the prefix "bat"
print(trie.get_words_with_prefix("bat"))  # Output: ['bat', 'battle']

# Search for words with a non-existing prefix
print(trie.get_words_with_prefix("cat"))  # Output: []
