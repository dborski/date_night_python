import unittest
from lib.binary_search_tree import BinarySearchTree

class BinarySearchTreeTest(unittest.TestCase):
  def setUp(self):
    self.search_tree = BinarySearchTree()
  
  def test_it_exists(self):
    self.assertIsInstance(self.search_tree, BinarySearchTree)
