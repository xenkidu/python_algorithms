""" Implementation of a Prefix Tree """
import string


class Trie:
    """ TODO: implement using TrieNodes """
    def __init__(self):
        self.root = dict()

    # inserts the given word and uses # as the terminal flag indicating a valid word.
    def insert(self, word: str) -> None:
        word = word.lower()
        node = self.root
        for c in word:
            if c not in node:
                node[c] = dict()
            node = node[c]
        node['#'] = 1

    # returns True if the word is in the trie.
    def search(self, word: str) -> bool:
        word = word.lower()
        node = self.root
        for c in word:
            if c not in node:
                node[c] = dict()
            node = node[c]
        return '#' in node

    # returns True if there exists a word with the given prefix.
    def starts_with(self, prefix: str) -> bool:
        prefix = prefix.lower()
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

    # returns all words with given prefix
    def get_words(self, prefix: str) -> list:
        prefix = prefix.lower()
        words = []
        stack = []
        node = self.root

        for c in prefix:
            if c not in node:
                return []
            node = node[c]

        stack.append((node, []))
        while stack:
            node, suffix = stack.pop()
            for key in node:
                if key != '#':
                    stack.append((node[key], suffix[:] + [key]))
            if '#' in node:
                words.append(prefix + ''.join(suffix))
        return words


if __name__ == '__main__':
    story = "Arthur Dent, whose house is about to be demolished for a planned road bypass, is lying down in front of a bulldozer when his friend Ford Prefect arrives and tells him that it is imperative that they go to the pub immediately. There Ford explains that he is actually from a planet near Betelgeuse and that another alien species, the Vogons, are about to destroy the Earth to make space for a hyperspatial express route. Meanwhile, Zaphod Beeblebrox, president of the Galaxy, and his human female friend Trillian steal the Heart of Gold spaceship. Ford and Arthur hitch a ride on a Vogon destructor ship, and Ford lends Arthur the electronic guidebook The Hitchhiker\'s Guide to the Galaxy and gives him a Babel fish to stick in his ear to translate alien speech. The Vogon ship captain has Ford and Arthur ejected into space, but the Heart of Gold, which has an Infinite Improbability Drive, picks them up 29 seconds later. The drive makes it possible to traverse interstellar space almost instantly but also causes Ford to (briefly) turn into a penguin.".translate(str.maketrans('', '', string.punctuation))

    trie = Trie()
    for word in story.split(' '):
        trie.insert(word)
    print(f'trie has "alien": {trie.search("alien")}')
    print(f'trie has words with prefix "sh": {trie.starts_with("sh")}')
    print(f'trie has words with prefix "interstellarz": {trie.starts_with("interstellarz")}')
    print(f'trie has words with prefix "Ga": {trie.starts_with("Ga")}')
    print(trie.get_words('g'))
    print(trie.get_words('hi'))

