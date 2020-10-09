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
  
  def test_next_left_is_none_by_default(self):
    self.assertEqual(self.node.next_left, None)

  def test_next_right_is_none_by_default(self):
    self.assertEqual(self.node.next_right, None)