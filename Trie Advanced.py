import keyboard # pip install keyboard
import trio # pip install trio

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words_from_node(node, prefix)

    def _find_words_from_node(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self._find_words_from_node(child_node, prefix + char))
        return words

# Create a Trie and insert words
trie = Trie()
words = [
    "apple", "banana", "orange", "grape", "watermelon", "pineapple", "strawberry", "blueberry", "raspberry", "blackberry",
    "mango", "papaya", "kiwi", "pear", "peach", "plum", "cherry", "apricot", "nectarine", "grapefruit",
    "lemon", "lime", "coconut", "fig", "pomegranate", "guava", "lychee", "dragonfruit", "jackfruit", "durian",
    "melon", "cantaloupe", "honeydew", "cranberry", "persimmon", "tangerine", "date", "olive", "avocado", "starfruit",
    "breadfruit", "elderberry", "gooseberry", "mulberry", "passionfruit", "quince", "tomato", "eggplant", "zucchini", "cucumber",
    "carrot", "beet", "radish", "turnip", "potato", "sweetpotato", "yam", "parsnip", "pumpkin", "squash",
    "cauliflower", "broccoli", "cabbage", "brusselsprouts", "kale", "spinach", "lettuce", "arugula", "collardgreens", "mustardgreens",
    "swisschard", "bokchoy", "fennel", "celery", "parsley", "cilantro", "basil", "oregano", "thyme", "rosemary",
    "sage", "dill", "mint", "tarragon", "chive", "garlic", "onion", "shallot", "leek", "scallion",
    "ginger", "turmeric", "horseradish", "wasabi", "cucumber", "zucchini", "squash", "pumpkin", "eggplant", "tomato",
    "bellpepper", "chilipepper", "jalapeno", "habanero", "serrano", "poblano", "pepper", "spinach", "lettuce", "kale",
    "arugula", "collardgreens", "swisschard", "mustardgreens", "endive", "escarole", "radicchio", "romaine", "bokchoy", "fennel",
    "celery", "carrot", "beet", "radish", "turnip", "potato", "sweetpotato", "yam", "parsnip", "rutabaga",
    "butternutsquash", "acornsquash", "spaghettisquash", "honeynutsquash", "delicatasquash", "kabocha", "pattypan", "zucchini", "yellowzucchini", "cucumber",
    "pickles", "corn", "peas", "greenbeans", "asparagus", "artichoke", "brusselsprouts", "broccoli", "cauliflower", "cabbage",
    "spinach", "kale", "collardgreens", "mustardgreens", "arugula", "lettuce", "romaine", "endive", "escarole", "radicchio",
    "watercress", "chard", "beetgreens", "turnipgreens", "dandeliongreens", "fiddleheadferns", "purslane", "sorrel", "amaranth", "bokchoy",
    "chineseleaf", "tatsoi", "mizuna", "komatsuna", "mustardspinach", "watermelon", "cantaloupe", "honeydew", "muskmelon", "crenshaw",
    "casaba", "sugarbaby", "canarymelon", "wintermelon", "cucumber", "picklingcucumber", "gherkin", "chayote", "bittermelon", "spaghetti",
    "spaghettisquash", "butternutsquash", "acornsquash", "delicatasquash", "kabocha", "pattypan", "carnival", "dumpling", "turban", "hubbard",
    "banana", "plantain", "mango", "papaya", "pineapple", "passionfruit", "kiwi", "starfruit", "dragonfruit", "rambutan",
    "lychee", "mangosteen", "durian", "jackfruit", "longan", "soursop", "custardapple", "cherimoya", "feijoa", "sapote"
]
for word in words:
    trie.insert(word)

async def async_input(prompt):
    print(prompt, end='', flush=True)
    buffer = []
    while True:
        event = await trio.to_thread.run_sync(keyboard.read_event)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'enter':
                print()  # Move to the next line
                break
            elif event.name == 'backspace':
                if buffer:
                    buffer.pop()
                    print('\b \b', end='', flush=True)
            else:
                buffer.append(event.name)
                print(event.name, end='', flush=True)
        word = ''.join(buffer)
        suggestions = trie.search(word)[:5]
        if suggestions:
            print(f"\nSuggestions: {', '.join(suggestions)}")
            print(f"{prompt}{word}", end='', flush=True)
    return ''.join(buffer)

async def main():
    word = await async_input('Enter the word: ')
    print(f'You entered: {word}')

trio.run(main)
