import unittest
from lib.binary_search_tree import BinarySearchTree

class BinarySearchTreeTest(unittest.TestCase):
  def setUp(self):
    self.tree = BinarySearchTree()
  
  def test_it_exists(self):
    self.assertIsInstance(self.tree, BinarySearchTree)

  def test_head_is_none_by_default(self):
    self.assertEqual(self.tree.head, None)
    