from node import Node
from graphviz import Digraph


class Bst:

  def __init__(self):
    self.node = None
    self.links = []

  def insertNode(self, node):
    new = Node(node)
    if self.node is None:
      self.node = new
    else:
      current = self.node
      while True:
        parent = current
        if node < current.val:
          current = current.left
          if current is None:
            parent.left = new
            self.links.append(str(parent.val) + '->' + str(new.val))
            return
        else:
          current = current.right
          if current is None:
            parent.right = new
            self.links.append(str(parent.val) + '->' + str(new.val))
            return

  def showLinks(self):
    return ' '.join(self.links)

  def findNode(self, node):
    current = self.node
    while current is not None:
      if node == current.val:
        return "Node " + str(node) + " found"
      elif node < current.val:
        current = current.left
      else:
        current = current.right
    return "Node " + str(node) + " not found"

  def orderTraversal(self, node, level=0) -> str:
    result = ''
    if node:
      result += self.orderTraversal(node.left, level + 1)
      result += ' ' * (level * 4) + str(node.val) + '\n'
      result += self.orderTraversal(node.right, level + 1)
    return result

  def preOrderTraversal(self, node, level=0) -> str:
    result = ''
    if node:
      result += ' ' * (level * 4) + str(node.val) + '\n'
      result += self.preOrderTraversal(node.left, level + 1)
      result += self.preOrderTraversal(node.right, level + 1)
    return result

  def postOrderTraversal(self, node, level=0) -> str:
    result = ''
    if node:
      result += self.postOrderTraversal(node.left, level + 1)
      result += self.postOrderTraversal(node.right, level + 1)
      result += ' ' * (level * 4) + str(node.val) + '\n'
    return result

  def deleteNode(self, value):
    if self.node is None:
      return "Tree is empty"

    current = self.node
    parent = self.node
    is_left_child = True

    while current.val != value:
      parent = current
      
      if value < current.val:
        is_left_child = True
        current = current.left
      else:
        is_left_child = False
        current = current.right

      if current is None:
        return "Node not found"

    if current.left is None and current.right is None:
      if current == self.node:
        self.node = None
      elif is_left_child:
        parent.left = None
      else:
        parent.right = None
        
    elif (current.right is None) or (current.left is not None and current.right is None):
      if current == self.node:
        self.node = current.left
      elif is_left_child:
        parent.left = current.left
      else:
        parent.right = current.left

    else: # Node has two children
      sucessor = self.getSucessor(current)

      if current == self.node:
        self.node = sucessor
      elif is_left_child:
        parent.left = sucessor
      else:
        parent.right = sucessor

      sucessor.left = current.left

    return "Node deleted"

  def getSucessor(self, node):
    parent_sucessor = node
    sucessor = node
    current = node.right

    while current is not None:
      parent_sucessor = sucessor
      sucessor = current
      current = current.left

    if sucessor != node.right:
      parent_sucessor.left = sucessor.right
      sucessor.right = node.right
      
    return sucessor

    