import pickle


class Trie:
    def __init__(self, *args):
        self.trie = {}
        for word in args:
            self.add(word)

    def add(self, *args):
        for word in args:
            if type(word) != str:
                raise TypeError("Trie only works on str!")
            temp_trie = self.trie
            for letter in word:
                temp_trie = temp_trie.setdefault(letter, {})
            temp_trie = temp_trie.setdefault('_', '_')

    def __contains__(self, word):
        if type(word) != str:
            raise TypeError("Trie only works on str!")
        temp_trie = self.trie
        for letter in word:
            if letter not in temp_trie:
                return False
            temp_trie = temp_trie[letter]
        return True

    def listHelp(self, temp, prefix, word):
        for letter in temp:
            if letter == "_":
                word.append(prefix)
            else:
                self.listHelp(temp[letter], prefix + letter, word)

    def list(self, prefix, words):
        root = self.trie
        if prefix == '':
            print("No prefix chosen")
        for i in root:
            if prefix == i:
                if i not in root:
                    return False
                else:
                    root = root[prefix]
                    self.listHelp(root, prefix, words)
                    print(words)

    def save(self):
        pickle.dump(self.trie, open('save.p', 'wb'))

    def load(self):
        self.trie = pickle.load(open('save.p', 'rb'))
        return(self.trie)