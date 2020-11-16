from lib.binary_search_tree import BinarySearchTree

tree = BinarySearchTree()

tree.load('./source/movies.txt')

import code; code.interact(local=dict(globals(), **locals()))