class Node:
    def __init__(self, children, is_a_word):
        self.children = children
        self.is_a_word = is_a_word


class Trie:
    def __init__(self):
        self.trie = None

    def build(self, words):
        self.trie = Node({}, False)
        for word in words:
            current = self.trie
            for char in word:
                if char not in current.children:
                    current.children[char] = Node({}, False)
                current = current.children[char]
            current.is_a_word = True

    def auto_complete(self, prefix):
        current = self.trie
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        return self.find_words_by_node(current, prefix)

    def find_words_by_node(self, node, prefix):
        words = []
        if node.is_a_word:
            words += [prefix]
        for char in node.children:
            words += self.find_words_by_node(node.children[char], prefix + char)
        return words


def main():
    phrase ="myccatisadickdodgemousethateatscarrotsinthedarkdarling"
    values = ['dog', 'dodge', 'cat', 'mouse', 'carrot', 'dark', 'darling']

    trie = Trie()
    trie.build(values)

    word = ''
    for char in phrase:
        word += char
        print(f'searching for: {word}')
        auto_complete_matches = trie.auto_complete(word)
        if auto_complete_matches:
            print(f'reviewing: {word}')
            print(f'found: {auto_complete_matches}')
        else:
            word = char


if __name__ == '__main__':
    main()
