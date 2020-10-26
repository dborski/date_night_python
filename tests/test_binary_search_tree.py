import unittest
from lib.binary_search_tree import BinarySearchTree

class BinarySearchTreeTest(unittest.TestCase):
  def setUp(self):
    self.tree = BinarySearchTree()
  
  def test_it_exists(self):
    self.assertIsInstance(self.tree, BinarySearchTree)

  def test_head_is_none_by_default(self):
    self.assertEqual(self.tree.head, None)

  def test_insert(self):
    self.assertEqual(self.tree.insert(61, "Bill & Ted's Excellent Adventure"), 0)
    self.assertEqual(self.tree.insert(16, "Johnny English"), 1)
    self.assertEqual(self.tree.insert(92, "Sharknado 3"), 1)
    self.assertEqual(self.tree.insert(50, "Hannibal Buress: Animal Furnace"), 2)
    self.assertEqual(self.tree.insert(60, "Die Hard"), 3)
    self.assertEqual(self.tree.insert(14, "Hot Tub Time Machine"), 2)
    self.assertEqual(self.tree.insert(19, "Catwoman"), 3)

  def test_has_score(self):
    self.tree.insert(61, "Bill & Ted's Excellent Adventure"), 0
    self.tree.insert(16, "Johnny English"), 1
    self.tree.insert(92, "Sharknado 3"), 1
    self.tree.insert(50, "Hannibal Buress: Animal Furnace"), 2
    self.tree.insert(60, "Die Hard"), 3
    self.tree.insert(14, "Hot Tub Time Machine"), 2
    self.tree.insert(19, "Catwoman"), 3

    self.assertEqual(self.tree.has_score(61), True)
    self.assertEqual(self.tree.has_score(16), True)
    self.assertEqual(self.tree.has_score(19), True)
    self.assertEqual(self.tree.has_score(72), False)
    self.assertEqual(self.tree.has_score(61), False)
    self.assertEqual(self.tree.has_score(15), False)
