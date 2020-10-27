from lib.node import Node

def _movie_payload(node):
  return {
    node.movie_title: node.movie_score
  }

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
    return self.score_depth_helper(movie_score, False, True, current_node)

  def depth_of(self, movie_score, current_node=None):
      return self.score_depth_helper(movie_score, None, False, current_node)
  
  def max(self, current_node=None):
    if current_node is None:
      current_node = self.head

    if current_node is None:
      return None
    else:
      if current_node.right:
        return self.max(current_node.right)
      else:
        return _movie_payload(current_node)
      
  def score_depth_helper(self, movie_score, first_return, second_return, current_node=None):
    if current_node is None:
      current_node = self.head

    if current_node is None:
      return first_return
    else:
      if current_node.movie_score == movie_score:
        return current_node.depth if second_return == False else second_return
      elif current_node.depth > 0 and current_node.left == None and current_node.right == None:
        return first_return
      else:
        return self.score_depth_helper(movie_score, first_return, second_return, current_node.right if movie_score > current_node.movie_score else current_node.left)


