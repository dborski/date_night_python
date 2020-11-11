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
    self.assertEqual(self.tree.has_score(3), False)

    self.tree.insert(61, "Bill & Ted's Excellent Adventure")
    self.tree.insert(16, "Johnny English")
    self.tree.insert(92, "Sharknado 3"), 1
    self.tree.insert(50, "Hannibal Buress: Animal Furnace")
    self.tree.insert(60, "Die Hard")
    self.tree.insert(14, "Hot Tub Time Machine")
    self.tree.insert(19, "Catwoman")

    self.assertEqual(self.tree.has_score(61), True)
    self.assertEqual(self.tree.has_score(16), True)
    self.assertEqual(self.tree.has_score(19), True)
    self.assertEqual(self.tree.has_score(72), False)
    self.assertEqual(self.tree.has_score(15), False)

  def test_depth_of(self):
    self.tree.insert(61, "Bill & Ted's Excellent Adventure")
    self.tree.insert(16, "Johnny English")
    self.tree.insert(92, "Sharknado 3")
    self.tree.insert(50, "Hannibal Buress: Animal Furnace")
    self.tree.insert(60, "Die Hard")
    self.tree.insert(14, "Hot Tub Time Machine")
    self.tree.insert(19, "Catwoman")

    self.assertEqual(self.tree.depth_of(92), 1)
    self.assertEqual(self.tree.depth_of(50), 2)
    self.assertEqual(self.tree.depth_of(60), 3)
    self.assertEqual(self.tree.depth_of(14), 2)
    self.assertEqual(self.tree.depth_of(13), None)
    self.assertEqual(self.tree.depth_of(87), None)

  def test_max_score(self):
    self.tree.insert(61, "Bill & Ted's Excellent Adventure")
    self.tree.insert(16, "Johnny English")
    self.tree.insert(92, "Sharknado 3")
    self.tree.insert(50, "Hannibal Buress: Animal Furnace")
    self.tree.insert(60, "Die Hard")
    self.tree.insert(14, "Hot Tub Time Machine")
    self.tree.insert(19, "Catwoman")

    expected = {
      "Sharknado 3": 92
    }

    self.assertEqual(self.tree.max(), expected)

  def test_min_score(self):
    self.tree.insert(61, "Bill & Ted's Excellent Adventure")
    self.tree.insert(16, "Johnny English")
    self.tree.insert(92, "Sharknado 3")
    self.tree.insert(50, "Hannibal Buress: Animal Furnace")
    self.tree.insert(60, "Die Hard")
    self.tree.insert(14, "Hot Tub Time Machine")
    self.tree.insert(19, "Catwoman")

    expected = {
      "Hot Tub Time Machine": 14
    }

    self.assertEqual(self.tree.min(), expected)

  def test_sort(self):
    self.tree.insert(61, "Bill & Ted's Excellent Adventure")
    self.tree.insert(16, "Johnny English")
    self.tree.insert(97, "Shrek")
    self.tree.insert(92, "Sharknado 3")
    self.tree.insert(50, "Hannibal Buress: Animal Furnace") 
    self.tree.insert(15, "Die Hard") 

    expected = [
      {"Die Hard": 15},
      {"Johnny English": 16},
      {"Hannibal Buress: Animal Furnace": 50},
      {"Bill & Ted's Excellent Adventure": 61},
      {"Sharknado 3": 92},
      {"Shrek": 97}
    ]

    self.assertEqual(self.tree.sort(), expected)

  def test_load(self):
    movie_list = open("./source/movies.txt", 'r').readlines()
    
    self.assertEqual(self.tree.load("./source/movies.txt"), 99)
