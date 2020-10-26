class Node:
  def __init__(self, movie_score, movie_title):
    self.movie_score = movie_score
    self.movie_title = movie_title
    self.left = None
    self.right = None
    self.depth = 0

  def insert(self, movie_score, movie_title):
    if self.movie_score > movie_score:
      return self.insert_left(movie_score, movie_title)

    elif self.movie_score < movie_score:
      return self.insert_right(movie_score, movie_title)
    else:
      return "That movie score has already been used. Please submit another one"
    
  def insert_left(self, movie_score, movie_title):
      if self.left == None:
        self.left = Node(movie_score, movie_title)
        self.left.depth = self.depth + 1
        return self.left.depth
      else:
        return self.left.insert(movie_score, movie_title)

  def insert_right(self, movie_score, movie_title):
      if self.right == None:
        self.right = Node(movie_score, movie_title)
        self.right.depth = self.depth + 1
        return self.right.depth
      else:
        return self.right.insert(movie_score, movie_title)


