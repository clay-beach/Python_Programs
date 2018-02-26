from Trie import Trie
from methods import Helpers
from pythonds import BinarySearchTree
from pythonds import AVLTree
import timeit

trie = Trie()
helper = Helpers()
binary = BinarySearchTree()
avl = AVLTree()

if __name__ == '__main__':
    file = open('words1.txt', 'r')
    string = ''
    for i in file:
        for word in i.split():
            word = word.lower()
            if word not in trie and word.isalpha() or word == "'":
                    trie.add(word)
                    binary.put(word, None)
                    avl.put(word, None)
            if word not in trie and '-' in word:
                helper.locate_hyphen(word, string)
                if word not in trie:
                    trie.add(string)
                    binary.put(word, None)
                    avl.put(word, None)
    file.close()

    Trie.save(trie)
    savedFile = Trie.load(trie)
    print('the saved file contains:', savedFile)

    # Generates a list from prefix
    prefix_list = []
    prefix = input('Please enter prefix')
    print('Your selected list contains:')
    Trie.list(trie, prefix, prefix_list)

    # Testing for trees
    print('Testing for tree structures:')
    exe = 0
    for i in range(10):
        start_time = timeit.default_timer()
        traverseBin = BinarySearchTree.inorder(binary)
        time = timeit.default_timer() - start_time
        exe += time
    average = exe / 10
    print('time to access words in binary tree:', average)

    exe2 = 0
    for i in range(10):
        start_time = timeit.default_timer()
        traverseAVL = AVLTree.inorder(avl)
        time = timeit.default_timer() - start_time
        exe2 += time
    average = exe2 / 10
    print('time to access words in AVL tree:', average)
