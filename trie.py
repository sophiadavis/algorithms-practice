import random

class Node(object):
    def __init__(self, letter):
        self.letter = letter
        self.children = []
        self.word_status = False

    def __repr__(self):
        return self.letter

def insert(current_node, word):
    first_letter = word[0]
    rest = word[1:]

    corresponding_child = next((child for child in current_node.children if child.letter == first_letter), None)

    if corresponding_child:
        if rest:
            insert(corresponding_child, rest)
        else:
            corresponding_child.word_status = True
            return

    else:
        node = Node(first_letter)
        current_node.children.append(node)
        if not rest:
            node.word_status = True
            return
        insert(node, rest)


def lookup(current_node, prefix, current = None):
    if not current:
        current = prefix
    first_letter = current[0]
    rest = current[1:]

    corresponding_child = next((child for child in current_node.children if child.letter == first_letter), None)

    if corresponding_child:
        if rest:
            lookup(corresponding_child, prefix, rest)
        else:
            print "Found words starting with: " + prefix
            generate_continuations(prefix[:-1], corresponding_child)

    else:
        print "No words starting with: " + prefix

def generate_continuations(prefix, current_node):
    if current_node.word_status:
        print prefix + current_node.letter
    for child in current_node.children:
        generate_continuations(prefix + current_node.letter, child)

def print_trie(root, level):
    for child in root.children:
        print '-'*level + str(child) + ' ' + str(child.word_status)
        print_trie(child, level + 1)

if __name__ == "__main__":
    with open("/usr/share/dict/words") as f:
        words = f.read()
    word_list = words.split('\n')

    # subset = random.sample(word_list, 1000)

    root = Node('')
    for word in word_list:#subset:
        if word:
            print "Adding " + word
            insert(root, word)

    # print_trie(root, 0)

    while True:
        prefix = raw_input("\nGive me a prefix to search > ")
        lookup(root, prefix)
        print
