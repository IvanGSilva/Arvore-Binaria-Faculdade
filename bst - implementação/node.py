class Node:

  def __init__(self, val: int):
    self.val: int = val
    self.left = None
    self.right = None

  def showVal(self):
    return self.val
