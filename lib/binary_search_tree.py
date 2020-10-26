from lib.node import Node

class BinarySearchTree:
  def __init__(self):
    self.head = None

  def insert(self, movie_score, movie_title):
    if self.head is None:
      self.head = Node(movie_score, movie_title)
      return self.head.depth
    else:
      return self.head.insert(movie_score, movie_title)

  def has_score(self, movie_score, current_node=None):
    if current_node is None:
      current_node = self.head

    if current_node is None:
      return False
    else:
      if current_node.movie_score == movie_score:
        return True
      elif current_node.depth > 0 and current_node.left == None and current_node.right == None:
        return False
      else:
        if movie_score > current_node.movie_score:
          return self.has_score(movie_score, current_node.right)
        else:
          return self.has_score(movie_score, current_node.left)
