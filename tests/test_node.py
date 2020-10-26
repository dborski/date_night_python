import unittest
from lib.node import Node

class NodeTest(unittest.TestCase):
  def setUp(self):
    self.node = Node(movie_score=60, movie_title="Hot Tub Time Machine")

  def test_it_exists(self):
    self.assertIsInstance(self.node, Node)

  def test_attributes(self):
    self.assertEqual(self.node.movie_score, 60)
    self.assertEqual(self.node.movie_title, "Hot Tub Time Machine")
  
  def test_left_is_none_by_default(self):
    self.assertEqual(self.node.left, None)

  def test_right_is_none_by_default(self):
    self.assertEqual(self.node.right, None)

  def test_insert_left(self):
    self.node.insert(56, "Bill & Ted's Excellent Adventure")

    self.assertEqual(self.node.left.movie_score, 56)

    self.node.insert(50, "Die Hard")

    self.assertEqual(self.node.left.left.movie_score, 50)

    self.assertEqual(self.node.insert(50, "Jingle Bells"), "That movie score has already been used. Please submit another one")

  def test_insert_right(self):
    self.node.insert(64, "Bill & Ted's Excellent Adventure")

    self.assertEqual(self.node.right.movie_score, 64)

    self.node.insert(70, "Die Hard")

    self.assertEqual(self.node.right.right.movie_score, 70)

    self.assertEqual(self.node.insert(60, "Jingle Bells"), "That movie score has already been used. Please submit another one"
    )