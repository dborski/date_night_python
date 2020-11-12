from lib.node import Node
import math

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
    return self.max_min_helper('max', current_node)
      
  def min(self, current_node=None):
    return self.max_min_helper('min', current_node)
  
  def height(self):
    return self.leaves()[1]
  
  def leaves(self):
    leaf_nodes = 0
    max_height = 0

    def recur(node):
      nonlocal leaf_nodes
      nonlocal max_height
      if not node:
        return 
      
      if not node.left and not node.right:
        leaf_nodes += 1
      
      if node.depth > max_height:
        max_height = node.depth
      
      recur(node.left)
      recur(node.right)
    
    recur(self.head)
    return leaf_nodes, max_height
  
  def load(self, text_file):
    movies = open(text_file, 'r')
    split_movies = movies.readlines()
    counter = 0

    for movie in split_movies:
      score, title = movie.split(", ", 1)
      insert_return = self.insert(int(score), title.rstrip())
      if isinstance(insert_return, int):
        counter += 1

    movies.close()
    return counter
  
  def health(self, depth):
    total_nodes = 0
    node_counts = {}
    payload = []

    def recur(node, saved_score=None):
      nonlocal total_nodes
      if not node:
        return

      saved_score = node.movie_score if node.depth == depth else saved_score
      total_nodes += 1

      if node.depth == depth:
        node_counts[saved_score] = 0

      if saved_score in node_counts:
        node_counts[saved_score] += 1

      recur(node.left, saved_score)
      recur(node.right, saved_score)

    recur(self.head)

    for score, value in node_counts.items():
      percentage = math.floor((float(value) / float(total_nodes)) * 100)
      payload.append([score, node_counts[score], percentage])

    return payload

  def sort(self):
    result = []

    def recur(node):
      if not node:
        return

      recur(node.left)
      result.append(_movie_payload(node))
      recur(node.right)

    recur(self.head)
    return result

  def max_min_helper(self, max_min, current_node=None):
    if current_node is None:
      current_node = self.head

    if current_node is None:
      return None
    else:
      if max_min == 'min' and current_node.left:
        return self.max_min_helper(max_min, current_node.left)
      elif max_min == 'max' and current_node.right:
        return self.max_min_helper(max_min, current_node.right)
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


